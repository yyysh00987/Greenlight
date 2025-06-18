from flask import Flask, request, jsonify
from flask_cors import CORS 
import pymysql.cursors
from pymysql.cursors import DictCursor
import os

app = Flask(__name__)
CORS(app)

#数据库配置
DB_CONFIG ={
    'host':'localhost',
    'user': 'gl_user',
    'password':'888566',
    'db':'greenlight_db',
    'charset': "utf8mb4",
    'cursorclass':DictCursor,
    'port': 3306
}

def get_db_connection():
   "" "获取数据库链接"""
   print("尝试连接数据库...") # 添加这行
   try:
        connection = pymysql.connect(**DB_CONFIG)
        print("MySQL/MariaDB 数据库连接成功！") # 添加这行
        return connection
   except Exception as e:
      print (f"数据库连接失败：{e}")
      return None

@app.route('/')
def home():
    return "oi!此乃grennlight后端API！"

# ===TodoList API ===

@app.route('/todos',methods=['POST'])
def add_todo():
    """添加一个新的todo"""
    data = request.json
    task =data.get('task')

    if not task:
        return jsonify({'error':'任务内容不能为空'}),400
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error':'数据库连接失败'}),500
    
    try:
        with connection.cursor() as cursor :
            sql ="INSERT INTO todos (task) VALUES (%s)"
            cursor.execute(sql,(task,))
        connection.commit()
        return jsonify({'message':'待办事项添加成功','id':cursor.lastrowid}),201
    except Exception as e:
        if connection :
            connection.rollback()
        return jsonify({'error': f'添加待办事项失败:{e}'}),500
    finally :
        if connection:
            connection.close()

@app.route('/todos',methods=['GET'])
def get_todos():
    """获取所有待办事项"""
    connection = get_db_connection()
    if connection is None :
        return jsonify({'error':'数据库连接失败'}),500
    
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id , task, is_completed, created_at FROM todos ORDER BY created_at DESC"
            cursor.execute(sql)
            todos =cursor.fetchall()
            return jsonify(todos), 200
    except Exception as e:
        return jsonify({'error': f'获取待办事项失败:{e}'}),500
    finally:
        if connection :
            connection.close()
        
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """更新待办事项状态"""
    data = request.json
    is_completed = data.get('is_completed')

    if is_completed is None:
        return jsonify({'error':'需要提供is_completed字段'}), 400

    connection = get_db_connection()
    if connection is None:
        return jsonify({'error':'数据库连接失败'}), 500
    
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE todos SET is_completed = %s WHERE id = %s"
            cursor.execute(sql, (is_completed, todo_id))
            connection.commit()
            if cursor.rowcount == 0:
                return jsonify({'message':'待办事项未找到或无需更新'}), 404
            return jsonify({'message':'待办事项更新成功'}), 200
    except Exception as e:
        return jsonify({'error': f'更新待办事项失败: {e}'}), 500
    finally:
        connection.close()

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """删除待办事项"""
    connection = get_db_connection()  # 拼写改正
    if connection is None:
        return jsonify({'error': '数据库连接失败'}), 500

    try:
        with connection.cursor() as cursor:  # 拼写改正
            sql = "DELETE FROM todos WHERE id = %s"
            cursor.execute(sql, (todo_id,))  # execute，参数要是元组，加逗号
            connection.commit()
            if cursor.rowcount == 0:
                return jsonify({'message': '待办事项未找到'}), 404
            return jsonify({'message': '待办事项删除成功'}), 200
    except Exception as e:
        connection.rollback()  # 拼写改正
        return jsonify({'error': f'删除待办事项失败: {e}'}), 500
    finally:
        connection.close()  # 拼写改正


if __name__ == '__main__':
    app.run(debug=True) #会在代码修改的时候自动重启服务器
