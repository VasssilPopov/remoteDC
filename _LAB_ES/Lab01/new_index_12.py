HEAD my_new_index

DELETE my_new_index



PUT /my_new_index
{
  "settings":{
	"index":{
	   "number_of_shards":1,
	   "number_of_shards":1
	},

    "analysis":{
       "filter":{
            "bulgarian_stemmer" : {
              "type" : "stemmer",
              "language" : "bulgarian"
            },
            "bulgarian_stop" : {
              "type" : "stop",
              "stopwords" : "_bulgarian_"
            }
      },
      "analyser":{
            "rebuilt_bulgarian" : {
              "filter" : [
                "lowercase",
                "bulgarian_stop",
                "bulgarian_stemmer"
              ],
              "char_filter" : ["html_strip"],
              "tokanizer":  "standard"}
            }
      }
  }
}



POST /my_new_index/_close



PUT my_new_index/_mapping/_doc 
{
  "properties" : {
    "date" : {
      "type" : "date",
      "format" : "yyyy.MM.dd"
    },
    "source" : {
      "type" : "keyword"
    },
    "text" : {
      "type" : "text",
      "analyzer" : "rebuilt_bulgarian"
    },
    "title" : {
      "type" : "text",
      "analyzer" : "rebuilt_bulgarian"
    },
    "url" : {
       "type" : "keyword"
    }
  }
}


POST /my_new_index/_open

GET my_new_index

POST _analyze
{
  "analyzer": "rebuilt_bulgarian",
  "text":     "Ние прочетохме много книги."
}

POST _analyze
{
  "analyzer": "rebuilt_bulgarian",
  "text":     "Прочетохме много книги."
}
