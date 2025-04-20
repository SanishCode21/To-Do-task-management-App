from flask_restful import Api, Resource, reqparse
from flask import request, jsonify
from flask_login import current_user
from application.models import Task, db

api = Api()

class TaskListAPI(Resource):
    def get(self):
        if not current_user.is_authenticated:
            return {"error": "Unauthorized"}, 401

        tasks = Task.query.filter_by(user_id=current_user.id).all()
        return [{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'priority': task.priority,
            'category': task.category,
            'due_date': task.due_date.isoformat() if task.due_date else None,
            'is_complete': task.is_complete
        } for task in tasks]

    def post(self):
        if not current_user.is_authenticated:
            return {"error": "Unauthorized"}, 401

        data = request.get_json()
        new_task = Task(
            title=data.get('title'),   # type: ignore
            description=data.get('description'),   # type: ignore
            priority=data.get('priority'),  # type: ignore
            category=data.get('category'),   # type: ignore
            due_date=data.get('due_date'),  # type: ignore
            user_id=current_user.id # type: ignore
        )
        db.session.add(new_task)
        db.session.commit()
        return {'message': 'Task created'}, 201
# Register routes (but don't bind app here)

class TaskAPI(Resource):
    def put(self, id):
        task = Task.query.get_or_404(id)
        if task.user_id != current_user.id:
            return {'message': 'Unauthorized'}, 403
        data = request.get_json()
        task.title = data['title']
        task.description = data.get('description', '')
        task.due_date = data.get('due_date')
        task.priority = data.get('priority', 'Low')
        task.category = data.get('category', '')
        task.is_complete = data.get('is_complete', False)
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'})

    def delete(self, id):
        task = Task.query.get_or_404(id)
        if task.user_id != current_user.id:
            return {'message': 'Unauthorized'}, 403
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'})

api.add_resource(TaskListAPI, '/api/tasks')
api.add_resource(TaskAPI, '/api/tasks/<int:id>')

