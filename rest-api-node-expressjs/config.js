// heroku Url ClearDb: mysql://b9d0204b9d5eeb:0f95c8cf@us-cdbr-east-05.cleardb.net/heroku_2742ddf698ff267?reconnect=true

const config = {
  db: {
    host: "localhost",
    user: "root",
    password: "",
    database: "hadits_api",
  },
  listPerPage: 10,
};
module.exports = config;
