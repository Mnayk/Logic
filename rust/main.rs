fn main() {
    // FROM: https://tourofrust.com/
    // RUN:  rustc rust/main.rs && ./main

    println!("Hello, world!");

    let x = 13;
    println!("{}", x);

    let x: f64 = 3.14159;
    println!("{}", x);

    let x;
    x = 0;
    println!("{}", x);

    let mut x = 42;
    println!("{}", x);

    x = 13;
    println!("{}", x);


    let x = 12;
    let a = 12u8;
    let b = 4.3;
    let c = 4.3f32;
    let bv = true;
    let t = (13, false);
    let sentence = "hello world!";
    println!(
        "{} {} {} {} {} {} {} {}",
        x, a, b, c, bv, t.0, t.1, sentence
    )
}
