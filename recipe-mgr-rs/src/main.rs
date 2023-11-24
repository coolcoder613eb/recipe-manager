use serde_json;
use serde_json::json;
use slint::{ModelRc, SharedString, VecModel};
use std::fs;
use std::rc::Rc;

const FILE_PATH: &str = "recipes.json";

fn load_data() -> serde_json::Value {
    match fs::read_to_string(FILE_PATH) {
        Ok(contents) => serde_json::from_str(&contents).unwrap(),
        Err(_) => serde_json::Value::Object(serde_json::Map::new()),
    }
}

fn save_data(data: &serde_json::Value) {
    fs::write(FILE_PATH, serde_json::to_string_pretty(data).unwrap()).unwrap();
}

fn open_editor() {
    let ew = EditWindow::new().unwrap();
    let weak = ew.as_weak();
    ew.on_return_from_editor(move |a, b, c| return_from_editor(&a, &b, &c, &weak.unwrap()));
    ew.show().unwrap();
}

fn new_recipe(window: &MainWindow) {
    
}

fn main() {
    /*
    let ew = EditWindow::new().unwrap();
    let weak = ew.as_weak();
    ew.on_return_from_editor(move |a, b, c| return_from_editor(&a, &b, &c, &weak.unwrap()));
    ew.run().unwrap();
    */
    let mut data = load_data();
    let window = MainWindow::new().unwrap();
    let recipes: Vec<SharedString> = data["recipes"]
        .as_array()
        .unwrap()
        .iter()
        .map(|recipe| SharedString::from(recipe["name"].as_str().unwrap()))
        .collect();
    let recipes_slice: &[SharedString] = &recipes;
    println!("{:?}", recipes_slice);
    window.set_recipes(VecModel::from_slice(recipes_slice));
    let weak = window.as_weak();
    window.on_new_recipe(move || new_recipe(&weak.unwrap()));
    window.run().unwrap();
}

fn return_from_editor(name: &str, desc: &str, ingredients: &str, ew: &EditWindow) {
    println!("Name: {name}, Desc: {desc}, Ingredients: {:?}", ingredients);
    let _ = ew.hide();
}

slint::slint! {
    import {Button, StandardButton, ListView} from "std-widgets.slint";
    export component MainWindow inherits Window {
        title: "Recipe Manager";
        min-width: 400px;
        min-height: 550px;
        in property<[string]> recipes: [];
        callback edit_recipe(int);
        callback delete_recipe(int);
        callback new_recipe();

        GridLayout {
            spacing: 30px;
            padding: 30px;
            Text {
                    max-height: 20px;
                    text: "Recipe Manager";
                    font-size: 18px;
                    font-weight: 600;
                    horizontal-alignment: center;
                    row: 0;
            }
             GridLayout {
                row: 1;
                spacing: 10px;
                Text {
                    max-height: 20px;
                    text: "Recipes";
                    font-size: 14px;
                    horizontal-alignment: center;
                    row: 0;
                }
                VerticalLayout {
                    row: 1;
                    ListView {
                        for recipe[index] in recipes: GridLayout{
                            padding-left: 10px;
                            padding-right: 10px;
                            spacing: 5px;
                            Text{
                                text: recipe;
                                font-size: 16px;
                                vertical-alignment: center;
                                horizontal-alignment: center;
                                col: 0;
                                colspan: 2;
                            }
                            Button {
                                col: 2;
                                max-width: 50px;
                                text: "Edit";
                                clicked => {edit_recipe(index);}
                            }
                            Button {
                                col: 3;
                                max-width: 60px;
                                text: "Delete";
                                clicked => {delete_recipe(index);}
                            }
                        }
                    }
                    Button {
                            text: "New Recipe ...";
                            clicked => {new_recipe();}
                    }
                }
            }

        }
    }
}

slint::slint! {
    import { LineEdit, TextEdit, StandardButton } from "std-widgets.slint";
    export component EditWindow inherits Window {
        title: "Recipe Editor";
        min-width: 400px;
        min-height: 550px;
        in-out property<string> ingredients: "Ingredient 1\nIngredient 2";
        in-out property<string> name: "Recipe name";
        in-out property<string> desc: "Recipe description";
        callback return_from_editor(string,string,string);
        GridLayout {
            spacing: 30px;
            padding: 30px;
            Text {
                max-height: 20px;
                text: "Recipe Editor";
                font-size: 18px;
                horizontal-alignment: center;
                row: 0;
            }
            GridLayout {
                row: 1;
                spacing: 10px;
                Text {
                    max-height: 20px;
                    text: "Recipe name";
                    font-size: 14px;
                    horizontal-alignment: center;
                    row: 0;
                }
                LineEdit {
                    max-height: 20px;
                    font-size: 14px;
                    placeholder-text: name;
                    row: 1;
                }
            }
            GridLayout {
                row: 2;
                spacing: 10px;
                Text {
                    max-height: 20px;
                    text: "Recipe description";
                    font-size: 14px;
                    horizontal-alignment: center;
                    row: 0;
                }
                LineEdit {
                    max-height: 20px;
                    font-size: 14px;
                    placeholder-text: desc;
                    row: 1;
                }
            }
            GridLayout {
                row: 3;
                spacing: 10px;
                Text {
                    max-height: 20px;
                    text: "Ingredients (one per line)";
                    font-size: 14px;
                    horizontal-alignment: center;
                    row: 0;
                }
                TextEdit {
                    font-size: 14px;
                    text: ingredients;
                    row: 1;
                }
            }
            StandardButton {
                row: 4;
                kind: ok;
                min-height: 40px;
                clicked => {
                    root.return_from_editor(name,desc,ingredients);
                }
            }
        }
    }
}
