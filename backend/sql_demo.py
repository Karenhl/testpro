from flask import Flask
from flask_sqlalchemy import SQLAlchemy


username = "root"
pwd = "123456"
ip = "localhost"
port = "3306"
database = "test"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120))

    def __repr__(self):
        return '<User %s>' % self.username


if __name__ == '__main__':
    # 创建
    # db.create_all()

    # 增加操作
    user1 = User(id=1, username='11', email='1@qq.com', gender='man')
    user2 = User(id=2, username='22', email='2@qq.com', gender='man')
    user3 = User(id=3, username='33', email='3@qq.com', gender='man')
    user4 = User(id=4, username='44', email='4@qq.com', gender='man')
    # 单个操作
    db.session.add(user1)
    # 批量操作
    db.session.add_all([user2, user3, user4])
    db.session.commit()
    #
    # # 查询操作
    # res = User.query.all()  # 查询所有
    # # 条件查询获取所有
    # res1 = User.query.filter_by(id=1).all()
    # # 条件查询获取第一条
    # res2 = User.query.filter_by(gender='男').first()
    # print(res.username, res.email, res.gender)
    # # 条件查询的其它方式
    # res3 = User.query.filter(User.id > 2).all()
    #
    # # 删除操作
    # User.query.filter_by(id=2).delete()
    # db.session.commit()
    #
    # # 修改操作
    # res = User.query.filter_by(id=3).first()
    # res.gender = "女"
    # db.session.commit()
    #
    # # 修改的第二种方式
    # res = User.query.filter_by(id=4).\
    #     update({"gender": "女", "email": "1234@qq.com", "username": "karen"})
    # db.session.commit()

