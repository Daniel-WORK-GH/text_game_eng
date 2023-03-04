# text game engine
a simple old school game "game engine".
easily build a simple traversable story using a json file

simple syntax:
```javascript
{
  "paths" : [ <--- list of story paths
    { <--- start of path
      "id" : "start", <--- path identifier
      "title" : "welcome, pick an option : ", <--- the displayed message
      "options" : [ <--- list of all possible outcomes
        { <--- start of option
          "sub_title" : "1.go to next", 
          "accepting" : [ <--- user input that will accept this options
            "1",
            "next"
          ],
          "goto" : "next"
        }
      ]
    },
    { 
      "id" : "next",
      "title" : "end of story",
      "options" : [] <--- nowhere to go from here
    }
  ]
}
```

this simple story will play out as follows :
welcome, pick an option : 
1.go to next
>>> 1
end of story
