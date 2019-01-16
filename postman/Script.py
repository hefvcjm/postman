# coding = utf-8

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

    def send_request(self, url, method, header, body, res):
        string = """
        // Example with a full fledged SDK Request
        const my_request = {
          url: "%s",
          method: "%s",
          header: "%s",
          body: {
            mode: 'raw',
            raw: "%s"
          }
        };
        pm.sendRequest(my_request, function (err, res) {
          if (err) {
              console.log(err);
          } else {
              "%s"
          }
        });
        
        """.replace("\n", "\r")
        self._script += (string % (url, method, header, body, res))

    def set_origin_js(self, code):
        self._script += code + "\r"

    def get_script(self):
        return self._script


class Test_Script(PreScript):

    def __init__(self):
        super().__init__()

    def test_status_code(self, description="Status code is 200", code="200"):
        self._script += ("""
        pm.test("%s", function () {
            pm.response.to.have.status(%s);
        });        
        """ % description, code)