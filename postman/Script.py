# coding = utf-8
import genson
import re


class PreScript:

    def __init__(self):
        self._script = ""

    def set_globals_environment(self, key, value):
        self._script += "       pm.globals.set(\"{}\", {});\r".format(str(key),
                                                                      "\"" + str(value) + "\"" if "{" not in str(
                                                                          value) else "JSON.stringify(%s)" % value)

    def set_environment(self, key, value):
        self._script += "       pm.environment.set(\"{}\", {});\r".format(str(key),
                                                                          "\"" + str(value) + "\"" if "{" not in str(
                                                                              value) else "JSON.stringify(%s)" % value)

    def get_globals_variable(self, var_name, var_key, is_json="no_json"):
        self._script += "       var {}=pm.globals.get(\"{}\");\r".format(var_name, var_key)
        if is_json == "json":
            self._script += "       %s=JSON.parse(%s);\r" % (var_name, var_name)

    def get_environment_variable(self, var_name, var_key, is_json="no_json"):
        self._script += "       var {}=pm.environment.get(\"{}\");\r".format(var_name, var_key)
        if is_json == "json":
            self._script += "       %s=JSON.parse(%s);\r" % (var_name, var_name)

    def clear_globals_variable(self, key):
        self._script += "pm.globals.unset(\"{}\");\r".format(key)

    def clear_environment_variable(self, key):
        self._script += "       pm.environment.unset(\"{}\");\r".format(key)

    def send_request(self, url, method, header, body, save, update):
        my_url = "\"" + url + "\""
        var = re.findall("{{.*?}}", url)
        s = re.split("{{.*?}}", url)
        if len(var) != 0:
            i = 0
            my_url = ""
            for item in var:
                item = item.replace("{", "").replace("}", "")
                self.get_globals_variable(item, item)
                if i != 0:
                    my_url = my_url + "+"
                my_url = my_url + "\"" + s[i] + "\"" + "+%s" % item
                i += 1
            # print(my_url)
        string = """
        // Example with a full fledged SDK Request
        var my_request = {
          url: %s,
          method: "%s",
          header: %s,
          body: {
            mode: 'raw',
            raw: %s
          }
        };
        pm.sendRequest(my_request, function (err, res) {
          if (err) {
              console.log(err);
          } else {
              %s
          }
        });
        
        """
        my_save = ""
        if save is not None:
            if "json" in save.keys():
                for a, b in zip(save["json"].keys(), save["json"].values()):
                    if a is not None:
                        temp = '.' + a
                    else:
                        temp = a
                    my_save += ("\r       pm.globals.set('%s',%s);\r" % (
                        b, "JSON.stringify(res.json()" + temp + ")"))
            if "no_json" in save.keys():
                for a, b in zip(save["no_json"].keys(), save["no_json"].values()):
                    if a is not None:
                        temp = '.' + a
                    else:
                        temp = a
                    my_save += ("       pm.globals.set('%s',%s);\r" % (b, "res.json()" + temp))
        if update is not None:
            for key in update.keys():
                my_save += "        var update_json=JSON.parse(pm.globals.get(\"{}\"));\r".format(key)
                update_info = update[key]
                for a, b in zip(update_info.keys(), update_info.values()):
                    temp = "        update_json.{}={};\r".format(a, b if not isinstance(b,
                                                                                        str) else "\"" + b + "\"").replace(
                        "\'", "\"")
                    var = re.findall("{{.*?}}", temp)
                    if len(var) != 0:
                        i = 0
                        for variable in var:
                            my_save += "        var temp{}=pm.globals.get(\"{}\");\r".format(
                                str(i), variable.replace("{", "").replace("}", ""))
                            temp = temp.replace("\"" + variable + "\"", "temp{}".format(str(i)))
                            i += 1
                    my_save += temp
                my_save += "        pm.globals.set(\"{}\", {});\r".format(key, "JSON.stringify(update_json)")
        headers = "\"\""
        data = "\"\""
        if header != {}:
            headers = str(header).replace("'", "\"")
            var = re.findall("{{.*?}}", str(header))
            if len(var) != 0:
                for item in var:
                    temp = item.replace("{", "").replace("}", "")
                    self.get_globals_variable(temp, temp)
                    headers = headers.replace("\"" + item + "\"", temp)
        if body != {}:
            data = str(body).replace("'", "\"")
            # print("0: ", data)
            if not re.match("^\".*?\"$", data):
                data = "\"" + data.replace("\"", "\\\"") + "\""
            var = re.findall("{{.*?}}", str(body))
            # print(var)
            if len(var) != 0:
                s = re.split("{{.*?}}", data)
                # print("1: ", data)
                # print(s)
                i = 0
                data = ""
                for item in var:
                    temp = item.replace("{", "").replace("}", "")
                    self.get_globals_variable(temp, temp)
                    data = data + s[i] + "\"+" + temp + "+\""
                    i += 1
                data = data + s[i]
                # data = data[1:]
                # print("3: ", data)
        # print(my_save)
        self._script += (string % (my_url, method, headers, data, my_save))

    def set_origin_js(self, code):
        self._script += code + "\r"

    def update_json_variable(self, key, update_info):
        string = "      var update_json=JSON.parse(pm.globals.get(\"{}\"));\r".format(key)
        for a, b in zip(update_info.keys(), update_info.values()):
            string += "     update_json.{}={};\r".format(a, b if not isinstance(b, str) else "\"" + b + "\"")
        string += "     pm.globals.set(\"{}\", {});\r".format(key, "JSON.stringify(update_json)")
        self._script += string

    def get_script(self):
        return self._script.replace("\n", "\r")


class TestScript(PreScript):

    def __init__(self):
        super().__init__()

    def test_status_code(self, description="Status code is 200", code="200"):
        description = "Status code is %s" % code
        string = """
        pm.test("%s", function () {
            pm.response.to.have.status(%s);
        });        
        """
        self._script += (string % (description, code))

    def test_response_json(self):
        string = """
        pm.test('返回json格式数据', () => {
            pm.response.to.be.json;
            pm.response.to.have.header('Content-Type', 'application/json;charset=UTF-8');
        });  
        
        """
        self._script += string

    def test_response_schema(self, json, description="json数据模式正确"):
        builder = genson.SchemaBuilder()
        builder.add_object(json)
        schema = builder.to_schema()
        self._script += ("""
        pm.test('%s', function() {
            var result=tv4.validateResult(JSON.parse(responseBody), %s);
            if(!result.valid){
                console.log(result);
            }
            pm.expect(result.valid).to.be.true;
        });
        """ % (description, schema))

    def test_response_json_has(self, keys, value):
        key = '.'.join(keys)
        string = """
        pm.test("%s字段为%s",function(){
            pm.expect(pm.response.json().%s).to.eql(%s);
        });
        
        """
        temp = value
        if isinstance(value, int) or isinstance(value, float):
            temp = str(temp)
        if isinstance(value, bool):
            temp = str(value).lower()
        if not (isinstance(value, int) or isinstance(value, float)) and not isinstance(value, bool):
            temp = "\'" + str(temp) + "\'"
        self._script += (string % (key, temp, key, temp))

    def test_response_json_has_variable(self, keys, var_type, key):
        json_key = '.'.join(keys)
        string = """
        var var_test = %s;
        pm.test("%s字段为"+"\\""+var_test+"\\"",function(){
            pm.expect(pm.response.json().%s).to.eql(var_test);
        });

        """
        temp = "pm.globals.get(\"%s\")"
        if var_type == "globals":
            temp = "pm.globals.get(\"%s\")"
        if var_type == "env":
            temp = "pm.environment.get(\"%s\")"
        if var_type == "var":
            temp = "pm.variable.get(\"%s\")"
        temp = temp % key
        self._script += (string % (temp, json_key, json_key))

    def test_has_string(self, value):
        string = """
        pm.test("Body matches '%s'", function () {
            pm.expect(pm.response.text()).to.include("%s");
        });
        
        """
        self._script += (string % (value, value))

    def test_has_variable(self, var_type, key):
        string = """
        var var_test = %s;
        pm.test("Body matches "+"\\""+var_test+"\\"", function () {
            pm.expect(pm.response.text()).to.include(var_test);
        });

        """
        temp = "pm.globals.get(\"%s\")"
        if var_type == "globals":
            temp = "pm.globals.get(\"%s\")"
        if var_type == "env":
            temp = "pm.environment.get(\"%s\")"
        if var_type == "var":
            temp = "pm.variable.get(\"%s\")"
        temp = temp % key
        self._script += (string % temp)

    def save_response(self, save_key, specific_keys=None, is_json="no_json"):
        if specific_keys is None:
            key = ""
        else:
            key = '.' + ('.'.join(specific_keys))
        string = """
        pm.globals.set("%s", %s);
        """
        self._script += (string % (
            save_key,
            "pm.response.json()" + key if is_json == "no_json" else "JSON.stringify(pm.response.json()" + key + ")"))

    def get_script(self):
        return self._script.replace("True", "true").replace("False", "false")


if __name__ == '__main__':
    script = TestScript()
    script.test_status_code()
    script.test_response_schema({"data": {}, "message": "", "code": 0, "success": False})
    print(script.get_script())
