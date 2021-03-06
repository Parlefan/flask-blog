#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
app管理程序
'''


import os

from app import create_app, db
from app.models import User, Role, Post

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


# 启动单元测试命令
@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests') # 测试用例加载器, 返回一个测试套件
    unittest.TextTestRunner(verbosity=2).run(tests) # 以文本形式显示测试结果



if __name__ == "__main__":
    manager.run()
