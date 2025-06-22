pub struct Solution;

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut x = x;
        let mut rev = 0;
        while x != 0 {
            let pop = x % 10;
            x /= 10;
            // Check for overflow/underflow before multiplying by 10
            if rev > i32::MAX / 10 || (rev == i32::MAX / 10 && pop > 7) {
                return 0;
            }
            if rev < i32::MIN / 10 || (rev == i32::MIN / 10 && pop < -8) {
                return 0;
            }
            rev = rev * 10 + pop;
        }
        rev
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example1() {
        assert_eq!(Solution::reverse(123), 321);
    }

    #[test]
    fn test_example2() {
        assert_eq!(Solution::reverse(-123), -321);
    }

    #[test]
    fn test_example3() {
        assert_eq!(Solution::reverse(120), 21);
    }
}
