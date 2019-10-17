import logging

import app


class UserLogin:
    def login(self, session, mobile, password):
        logging.info("登录操作")
        return session.post(app.BASE_URL + "login", json={"mobile": mobile,
                                                          "password": password,
                                                          })
