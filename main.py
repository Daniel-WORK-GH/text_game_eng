import json
import structure

def load_story(story_path : str) -> structure.Root : 
    story_string : str
    with open("story\\temp.json") as file:
        story_string = file.read()

    jsonstring = json.loads(story_string)
    return structure.Root.from_dict(jsonstring)

def get_next_path(story_root : structure.Root, root_id : str) -> structure.Path :
    for p in story_root.paths:
        if p.id == root_id:
            return p

def get_path_from_input(path : structure.Path, selection : str) -> structure.Path :
    for o in path.options:
        if selection in o.accepting:
            return o.goto

def execute_path(path : structure.Path) -> str :
    while True:
        print(f"\n{path.title}")

        for o in path.options:
            print(o.sub_title)

        next_id = get_path_from_input(path, input()) 
        if next_id != None:
            return next_id
        else :
            print("Hmm try picking a diffrent option.")

def is_eop(path : structure.Path):
    return len(path.options) == 0

def execute_story(story_root : structure.Root) -> None:
    current_path = get_next_path(story_root, "start")
    while not is_eop(current_path):
        current_path = get_next_path(story_root, execute_path(current_path))
    print(current_path.title)
    
story = load_story("story\\temp.json")
execute_story(story)
