from .bot import main 

if __name__ == '__main__': 
    try: 
        main() 
    except KeyBoardInterrupt: 
        pass 

