from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


username = "root"
pwd = "123456"
ip = "localhost"
port = "3306"
database = "test"

# 实例化flask对象
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'


db = SQLAlchemy(app)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))


class TestCaseService(Resource):
    """
    测试用例服务
    """
    # 查询用例
    def get(self):
        case_id = request.args.get("id")
        if case_id:
            # 查询单条数据信息
            case_data = TestCase.query.filter_by(id=case_id).first()
            app.logger.info(case_data)
            data = [{"id": case_data.id, "nodeid": case_data.nodeid, "remark": case_data.remark}]
        else:
            # 查询所有的参数
            case_data = TestCase.query.all()
            data = {}
            for i in case_data:
                data["id"] = i.id
                data["nodeid"] = i.nodeid
                data["remark"] = i.remark

        app.logger.info(data)
        return {"eroor": 0, "msg": {"data": data}}

    # 增加用例
    def post(self):
        # 增加一条用例
        case_data = request.json
        app.logger.info(case_data)
        # 从接口中拿到的字典数据进行解包，使用关键字传参
        testcase = TestCase(**case_data)
        db.session.add(testcase)
        db.session.commit()
        return {"eroor": 0, "msg": "get sucess"}

    # 修改用例
    def put(self):
        # 获取被修改的信息
        case_id = request.json.get("id")
        # 找到被修改的信息再做修改操作
        case = TestCase.query.filter_by(id=case_id).update(request.json)
        app.logger.info(case)
        return {"eroor": 0, "msg": {"id": case}}

    # 删除用例
    def delete(self):
        # 获取被修改的信息
        case_id = request.json.get("id")
        # 找到被修改的信息再删除
        case = TestCase.query.filter_by(id=case_id)
        case.delete()
        db.session.commit()
        return {"eroor": 0, "msg": {"data": case_id}}


if __name__ == "__main__":
    # db.create_all()
    api.add_resource(TestCaseService, "/testcase")
    app.run(debug=True)
