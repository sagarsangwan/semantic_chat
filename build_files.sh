
pip install -r requirements.txt
echo "Making migrations..."
python3.9 manage.py makemigrations --noinput

python3.9 manage.py migrate
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear