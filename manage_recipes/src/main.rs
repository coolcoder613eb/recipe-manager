use std::fs;
use serde_json;
use serde_json::json;
use std::io;
use std::io::Write;
use std::process::Command;

const FILE_PATH: &str = "recipes.json";

// function to print without newline
fn print(message: &str) {
    print!("{}", message);
    // doesn't display otherwise
    let _ = io::stdout().flush();
}

fn load_data() -> serde_json::Value {
    match fs::read_to_string(FILE_PATH) {
        Ok(contents) => serde_json::from_str(&contents).unwrap(),
        Err(_) => serde_json::Value::Object(serde_json::Map::new()),
    }
}

fn save_data(data: &serde_json::Value) {
    fs::write(FILE_PATH, serde_json::to_string_pretty(data).unwrap()).unwrap();
}

fn edit_text(name: &str) -> String {
    loop {
        if cfg!(target_os = "windows") {
            Command::new("hecto.exe").arg(name).spawn().expect("Failed to open Hecto");
        } else {
            Command::new("nano").arg("-R").arg("-m").arg("-n").arg(name).spawn().expect("Failed to open Nano");
        }

        match fs::read_to_string(name) {
            Ok(text) => {
                if !text.is_empty() {
                    break text;
                }
            }
            Err(_) => continue,
        }
    }
}

fn list_recipes(data: &serde_json::Value, parent_name: Option<&str>) {
    let recipes = data["recipes"].as_array().unwrap();

    for (i, recipe) in recipes.iter().enumerate() {
        if let Some(parent) = parent_name {
            println!("{} -> {}. {} - {}", parent, i + 1, recipe["name"], recipe["desc"]);
        } else {
            println!("{}. {} - {}", i + 1, recipe["name"], recipe["desc"]);
        }
    }
}

fn create_recipe(mut data: &mut serde_json::Value) {
    let mut name = String::new();
    print("Enter the name of the recipe: ");
    io::stdin().read_line(&mut name).expect("Failed to read input");
    let name = name.trim();

    let mut desc = String::new();
    print("Enter the description: ");
    io::stdin().read_line(&mut desc).expect("Failed to read input");
    let desc = desc.trim();

    let is_subrecipe = false; // Uncomment this line to allow sub-recipes

    if is_subrecipe {
        // Logic for sub-recipes
    } else {
        println!("Enter the ingredients, one per line, then save and exit.");
        println!("Press Enter to start.");
        let ingredients: String = edit_text("name").split('\n').map(|s| s.to_string()).collect();

        println!("Enter the instructions, then save and exit.");
        println!("Press Enter to start.");
        let instructions = edit_text("name");

        let recipe = json!({
            "name": name,
            "desc": desc,
            "ingredients": ingredients,
            "instructions": instructions,
        });

        data["recipes"].as_array_mut().unwrap().push(recipe);
        save_data(&data);
        println!("Recipe added successfully.");
    }
}

// Functions like read_recipe, update_recipe, delete_recipe should be implemented similarly

fn main() {
    let mut data = load_data();

    loop {
        println!("\nRecipe Manager\n");
        println!("1. List recipes");
        println!("2. Create a recipe");
        println!("3. Read a recipe");
        println!("4. Update a recipe");
        println!("5. Delete a recipe");
        println!("6. Exit");

        print("\nEnter your choice: ");

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read input");
        let choice = choice.trim();

        match choice {
            "1" => list_recipes(&data, None),
            "2" => create_recipe(&mut data),
            "3" => {
                print("Enter the index of the recipe: ");
                let mut index_str = String::new();
                io::stdin().read_line(&mut index_str).expect("Failed to read input");
                let index = index_str.trim().parse().unwrap_or(0) - 1;
                // read_recipe logic here
            }
            "4" => {
                print("Enter the index of the recipe: ");
                let mut index_str = String::new();
                io::stdin().read_line(&mut index_str).expect("Failed to read input");
                let index = index_str.trim().parse().unwrap_or(0) - 1;
                // update_recipe logic here
            }
            "5" => {
                print("Enter the index of the recipe: ");
                let mut index_str = String::new();
                io::stdin().read_line(&mut index_str).expect("Failed to read input");
                let index = index_str.trim().parse().unwrap_or(0) - 1;
                // delete_recipe logic here
            }
            "6" => break,
            _ => println!("Invalid choice. Please try again."),
        }
    }
}
