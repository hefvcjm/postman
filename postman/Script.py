# coding = utf-8
import genson


class PreScript:

    def __init__(self):
        self._script = ""

    def set_global_environment(self, key, value):
        self._script += "pm.globals.set(\"{}\", \"{}\");\r".format(str(key), str(value))

    def set_environment(self, key, value):
        self._script += "pm.environment.set(\"{}\", \"{}\");\r".format(str(key), str(value))

    def get_global_variable(self, var_name, var_key):
        self._script += "var {}=pm.globals.get(\"{}\");\r".format(var_name, var_key)

    def get_environment_variable(self, var_name, var_key):
        self._script += "var {}=pm.environment.get(\"{}\");\r".format(var_name, var_key)

    def clear_global_variable(self, key):
        self._script += "pm.globals.unset(\"{}\");\r".format(key)

    def clear_environment_variable(self, key):
        self._script += "pm.environment.unset(\"{}\");\r".format(key)

    def send_request(self, url, method, header, body, res_save, keys):
        string = """
        // Example with a full fledged SDK Request
        const my_request = {
          url: "%s",
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
        save = ""
        for a, b in zip(res_save, keys):
            if b is not None:
                temp = '.' + b
            else:
                temp = b
            save += ("          pm.environment.set('%s',res.json()%s);\r" % (a, temp))
        headers = "\"\""
        data = "\"\""
        if header != {}:
            headers = header
        if body != {}:
            data = body
        self._script += (string % (url, method, headers, data, save))

    def set_origin_js(self, code):
        self._script += code + "\r"

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

    def test_has_string(self, value):
        string = """
        pm.test("Body matches '%s'", function () {
            pm.expect(pm.response.text()).to.include("%s");
        });
        
        """
        self._script += (string % (value, value))

    def save_response(self, save_key, specific_keys=None):
        if specific_keys is None:
            key = ""
        else:
            key = '.' + ('.'.join(specific_keys))
        string = """
        pm.environment.set("%s", pm.response.json()%s);
        """
        self._script += (string % (save_key, key))

    def get_script(self):
        return self._script


if __name__ == '__main__':
    script = TestScript()
    script.test_status_code()
    script.test_response_schema({"data": {}, "message": "", "code": 0, "success": False})
    print(script.get_script())
