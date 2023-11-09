fn main() {
    EditWindow::new().unwrap().run().unwrap();
}

slint::slint! {
    import { LineEdit, TextEdit, StandardButton } from "std-widgets.slint";
    export component EditWindow inherits Window {
        title: "Recipe Editor";
        min-width: 400px;
        min-height: 550px;
        in-out property<string> ingredients: "Ingredient 1\nIngredient 2";
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
                    text: "Recipe title";
                    font-size: 14px;
                    horizontal-alignment: center;
                    row: 0;
                }
                LineEdit {
                    max-height: 20px;
                    font-size: 14px;
                    placeholder-text: "Recipe title";
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
                    placeholder-text: "Recipe description";
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
            }
        }
    }
}