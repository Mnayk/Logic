const PI: f32 = 3.14159;

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
    );

    let a = 13u8;
    let b = 7u32;
    let c = a as u32 + b;
    println!("{}", c);

    let t = true;
    println!("{}", t as u8);

    // const
    println!(
        "To make an apple {} from scratch, you must first create a universe.",
        PI
    );

    // array
    let nums: [i32; 3] = [1, 2, 3];
    println!("{:?}", nums);
    println!("{}", nums[1]);

    //functions
    fn add(x: i32, y: i32) -> i32 {
        return x + y;
    }
    println!("{}", add(42, 13));

    //tuple swap
    fn swap(x: i32, y: i32) -> (i32, i32) {
        return (y, x);
    }

    let result = swap(123, 321);
    println!("{} {}", result.0, result.1);

    let (a, b) = swap(result.0, result.1);
    println!("{} {}", a, b)
}
