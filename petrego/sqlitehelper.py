"""This module contains all the methods to interact with the database.
"""
from petrego.db import get_db

class SQLiteHelper():
    """SQLite Database helper class.
    """
    @staticmethod
    def insert_animal_food(animal, food, error):
        db = get_db()

        try:
            db.execute('INSERT INTO food (name) VALUES (?)', (food,))
        except:
            pass
        try:
            db.execute('INSERT INTO animal (name) VALUES (?)', (animal,))
        except:
            pass
        try:
            db.execute(
                'INSERT INTO animal_food (animal_id, food_id) ' +
                'SELECT a.id, f.id FROM animal a, food f ' +
                'WHERE a.name = ? AND f.name = ?', (animal, food)
                )
        except Exception as ex:
            db.rollback()
            error = str(ex)
            return False

        db.commit()
        return True

    @staticmethod
    def update_animal_food(animal, food, error):
        db = get_db()

        try:
            db.execute('INSERT INTO food (name) VALUES (?)', (food,))
        except:
            pass

        try:
            db.execute(
                'UPDATE animal_food ' +
                'SET food_id = (SELECT id FROM food WHERE name = ?) ' +
                'WHERE animal_id = (SELECT id FROM animal WHERE name = ?)'
                , (food, animal)
                )
        except Exception as ex:
            db.rollback()
            error = str(ex)
            return False

        db.commit()
        return True

    @staticmethod
    def get_animal_food(animal):
        db = get_db()

        res = db.execute(
            'SELECT a.name AS animal, f.name AS food FROM animal_food af ' +
            'INNER JOIN animal a ON a.id = af.animal_id ' +
            'INNER JOIN food f ON f.id = food_id ' +
            'WHERE a.name = ? ',
            (animal,)
        ).fetchall()

        return res

    @staticmethod
    def get_animals():
        db = get_db()

        res = db.execute(
            'SELECT name from animal'
        ).fetchall()

        return res

    @staticmethod
    def insert_owner(first_name, last_name, error):
        db = get_db()

        try:
            db.execute(
            'INSERT INTO owner (first_name, last_name) VALUES (?, ?)',
            (first_name, last_name))
        except Exception as ex:
            db.rollback
            error = str(ex)
            return False

        db.commit()
        return True

    @staticmethod
    def get_owners():
        db = get_db()

        res = db.execute(
            'SELECT first_name, last_name from owner'
        ).fetchall()

        return res

    @staticmethod
    def insert_pet(first_name, last_name, pet_name, pet_type, error):
        db = get_db()

        try:
            db.execute(
            'INSERT INTO pet (owner_id, animal_id, name) ' +
            'SELECT o.id , a.id, ? FROM animal a, owner o ' +
            'WHERE a.name = ? AND o.first_name = ? AND o.last_name = ?',
            (pet_name, pet_type, first_name, last_name)
            )
        except Exception as ex:
            db.rollback
            error = str(ex)
            return False
        db.commit()
        return db.total_changes > 0

    @staticmethod
    def get_pets(first_name, last_name):
        db = get_db()

        res = db.execute(
            'SELECT o.first_name, o.last_name, p.name AS pet_name, ' +
            'a.name AS pet_type, f.name AS food_name FROM pet p ' +
            'INNER JOIN owner o ON o.id = p.owner_ID ' +
            'INNER JOIN animal a ON a.id = p.animal_id ' +
            'INNER JOIN animal_food af on af.animal_id = a.id ' +
            'INNER JOIN food f on f.id = af.food_id ' +
            'WHERE o.first_name = ? AND o.last_name = ?',
            (first_name, last_name)
        ).fetchall()

        return res

    @staticmethod
    def delete_pet(pet_name, first_name, last_name):
        db = get_db()

        try:
            res = db.execute(
                'DELETE FROM pet WHERE pet.owner_id = '+
                '(select o.id from owner o ' +
                'where o.first_name=? and o.last_name=?) and pet.name = ?',
                (first_name, last_name, pet_name)
            )
        except Exception as ex:
            db.rollback
            error = str(ex)
            return False
        db.commit()
        return db.total_changes > 0
