from sqlalchemy import column,Integer,String

class User(base):
    __tablename__ = 'users'
    id = column(Integer, primary_key=True)
    username = column(String(64), nullable=False)
    password = column(String(64), nullable=False)
    email = column(String(120), nullable=False)
    created_at = column(String(64), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
