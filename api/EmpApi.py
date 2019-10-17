import app


class EmpCRUD:
    def add(self, session, username, mobile, workNumber):
        myAddEmp = {"username": username,
                    "mobile": mobile,
                    "workNumber": workNumber
                    }
        return session.post(app.BASE_URL + "user", json=myAddEmp, headers={"Authorization": "Bearer " + app.TOKEN})

    def update(self, session, userId, username):
        return session.put(app.BASE_URL + "user/" + userId,
                           json={"username": username},
                           headers={"Authorization": "Bearer " + app.TOKEN})

    def get(self, session, userId):
        return session.get(app.BASE_URL + "user/" + userId,
                           headers={"Authorization": "Bearer " + app.TOKEN})

    def delete(self, session, userId):
        return session.delete(app.BASE_URL + "user/" + userId,
                              headers={"Authorization": "Bearer " + app.TOKEN})
