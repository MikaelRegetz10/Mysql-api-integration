from models.connection import db


def select_all_infos():
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT id as id, name as name, buy as buy, sell as sell, type as type, link as link FROM consumiveis")
        result = cursor.fetchall()
        cursor.close()

        return {"status": True, "data": result}

    except Exception as e:
        print(e)
        return {"status": False, "data": "deu ruim"}


def add_new_consumable(name, buy, sell, type, link):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("INSERT consumiveis (name, buy, sell, type, link) VALUES (%s, %s, %s, %s, %s)", (name, buy, sell, type, link))
        db.commit()

        cursor.execute("SELECT id as id, name as name, buy as buy, sell as sell, type as type, link as link FROM consumiveis")
        result = cursor.fetchall()
        cursor.close()

        return {"status": True, "data": result}
    except Exception as e:
        print(e)
        return {"status": False, "data": "deu ruim"}


def delete_consumable(id):
    try:
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT id as id, name as name, buy as buy, sell as sell, type as type, link as link FROM consumiveis")
        results = cursor.fetchall()
        for result in results:
            if result['id'] == id:
                cursor.execute("DELETE FROM consumiveis WHERE id = %s", (id,))
                db.commit()
                cursor.close()
                return {"status": True, "data": results, "not_fould":False}

        return {"status": True, "data": results, "not_fould": True}

    except Exception as e:
        db.rollback()
        print(e)
        return {"status": False, "data": "deu ruim"}

