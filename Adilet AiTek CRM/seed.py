from database import SessionLocal
import models

db = SessionLocal()

try:
    # 1. Создаем филиалы
    almaty = models.Branch(name="Алматы", city="Алматы")
    astana = models.Branch(name="Астана", city="Астана")
    db.add_all([almaty, astana])
    db.commit()
    db.refresh(almaty)
    db.refresh(astana)

    # 2. Создаем сотрудников
    users = [
        # Общие / сидящие в Алматы на оба филиала
        models.User(name="Темирлан Канатович", role="Начальник отдела логистики", branch_id=almaty.id),
        models.User(name="Жулдыз Батырбек", role="Бухгалтер", branch_id=almaty.id),
        models.User(name="Адилет Бекенович", role="Главный технический специалист", branch_id=almaty.id),
        
        # Менеджеры и сотрудники по филиалам
        models.User(name="Ұлпан", role="Manager (Алматы)", branch_id=almaty.id),
        models.User(name="БАХА", role="Manager (Алматы)", branch_id=almaty.id),
        models.User(name="Аида", role="Director (Астана)", branch_id=astana.id),
        models.User(name="Аружан", role="ОКК (Астана)", branch_id=astana.id),
    ]
    db.add_all(users)
    db.commit()

    # 3. Создаем тестового клиента
    client = models.Client(name="Оразбай Жансая", phone="87770987654", branch_id=almaty.id)
    db.add(client)
    db.commit()

    print("База успешно заполнена реальным списком сотрудников!")
except Exception as e:
    db.rollback()
    print(f"Ошибка при заполнении: {e}")
finally:
    db.close()