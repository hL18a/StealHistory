
import historial1
import historial2 
import delete

def main():
   
    try:
        historial1.historial_defuald_ataque()
    except Exception as e:
        pass

    try:
        historial2.history_user_data_ataque()
    except Exception as e:
        pass

    try:
        delete.auto_delete()
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
