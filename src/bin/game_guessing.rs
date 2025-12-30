use std::io;
use std::cmp::Ordering;

fn main() {
    println!("Угадай число!");

    let secret_number = rand::random_range(1..=100);

    loop {
        println!("Введите ваше предположение:");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Не удалось прочитать строку");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        
        println!("Вы предположили: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Слишком маленькое!"),
            Ordering::Greater => println!("Слишком большое!"),
            Ordering::Equal => {
                println!("Вы угадали!");
                break;
            }
        }
    }
}
