python manage.py validate 
@echo "if 0 error"
@echo "继续执行添加到数据库"
@pause
@echo "Library 可以替换为别的app"
python manage.py sqlall Library
@pause