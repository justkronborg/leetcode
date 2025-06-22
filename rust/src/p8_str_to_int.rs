pub struct Solution;

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let s = s.trim_start();
        let mut chars = s.chars().peekable();
        let mut sign = 1;
        if let Some(&c) = chars.peek() {
            if c == '-' {
                sign = -1;
                chars.next();
            } else if c == '+' {
                chars.next();
            }
        }
        let mut result: i64 = 0;
        while let Some(&c) = chars.peek() {
            if let Some(d) = c.to_digit(10) {
                result = result * 10 + d as i64;
                if sign == 1 && result > i32::MAX as i64 {
                    return i32::MAX;
                }
                if sign == -1 && -result < i32::MIN as i64 {
                    return i32::MIN;
                }
                chars.next();
            } else {
                break;
            }
        }
        (sign * result as i64).clamp(i32::MIN as i64, i32::MAX as i64) as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example1() {
        assert_eq!(Solution::my_atoi("42".to_string()), 42);
    }

    #[test]
    fn test_example2() {
        assert_eq!(Solution::my_atoi(" -042".to_string()), -42);
    }

    #[test]
    fn test_example3() {
        assert_eq!(Solution::my_atoi("1337c0d3".to_string()), 1337);
    }

    #[test]
    fn test_example4() {
        assert_eq!(Solution::my_atoi("0-1".to_string()), 0);
    }

    #[test]
    fn test_example5() {
        assert_eq!(Solution::my_atoi("words and 987".to_string()), 0);
    }
}
