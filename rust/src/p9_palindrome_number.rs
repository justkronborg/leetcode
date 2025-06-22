pub struct Solution;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        let s = x.to_string();
        s.chars().eq(s.chars().rev())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        assert!(Solution::is_palindrome(121));
    }

    #[test]
    fn example2() {
        assert!(!Solution::is_palindrome(-121));
    }

    #[test]
    fn example3() {
        assert!(!Solution::is_palindrome(10));
    }
}
