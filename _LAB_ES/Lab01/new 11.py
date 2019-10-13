PUT /my_new_index
{
  "settings":{
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
  },
    "mappings" : {
      "_doc" : {
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
    }
}