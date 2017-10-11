CREATE  TABLE calendar (
  id INTEGER  PRIMARY KEY AUTOINCREMENT ,
  data_create DATE not NULL ,
  start_data DATE not NULL ,
  end_data date not null DEFAULT  CURRENT_TIMESTAMP,
  STATUS INTEGER CHECK (STATUS =1 or STATUS=0) NOT NULL DEFAULT 0,
  text TEXT NOT NULL DEFAULT '-'
);