from flask_restx import Namespace, Resource    # RESTful API
from flaskr.extensions import db       # 导入数据库
import flaskr.models  # 务必导入模型,不然db语句无法知道模型,也就不能创建表

api = Namespace('database', description='数据库操作接口')


@api.route('/create')
class Create(Resource):
    @api.doc(description='创建数据库,只用执行一次。重复执行视为测试数据库连接')
    def get(self):
        """
        创建数据库
        """
        try:
            db.create_all()
            return 200
        except:
            return 500


@api.route('/drop')
class Drop(Resource):
    @api.doc(description='删除数据库')
    def get(self):
        """
        删除数据库
        """
        try:
            db.drop_all()
            return 200
        except:
            return 500
