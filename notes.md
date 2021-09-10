### Structure 

start with the basics, we need a bot that can connect to the binance API 
- stream price data for a selected asset 
- Place orders trough the binance API



### Build this Feature by Feature 

- Features of this bot 
    # Api server 
    - What does it do
    - Connects clients to the Coin data 

     # Binance API Manager:
      - Wrapper to handle the Binance API 
      - It depends on BInance stream manager

    # Auto Trader
        - It handles order execution and scouts for trading signals in the market 
        - It depends on the API manager


    # Binance Stream Manager

    # Backetester 
        - Strategy backtesting module
        - It depends on the models package, binance_api_manager, binance_stream_manager

    # Config 
        - Application configuration 
        - It depends on the models package 

    # Crypto trading: 
        - The main trading loop 
        - It depends on the 
          - Api manager 
          - config 
          - logger 
          - scheduler 
          - strategies

    # Database: 
        - The database ORM (engine)
        - Depends on:
          - config
          - logger 
          - models

    # Logger: 
        - Logs and log files management
        - Depends on notification

    # Notifications: 
        - Queueing mechanism and messages

    # Job Scheduler (scheduler.py): 
        - Running jobs that may or may not crash without worrying about whether other jobs will run 
        - or

    # Strategies: 
        - module implementing different trading strategies 
        - Depends on 
          - auto_trader


    # Models: 
        - The data models of the API