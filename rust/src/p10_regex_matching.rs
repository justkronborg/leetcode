pub struct Solution;

impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let s = s.as_bytes();
        let p = p.as_bytes();
        let (m, n) = (s.len(), p.len());
        let mut dp = vec![vec![false; n + 1]; m + 1];
        dp[0][0] = true;

        for j in 1..=n {
            if p[j - 1] == b'*' && j >= 2 {
                dp[0][j] = dp[0][j - 2];
            }
        }

        for i in 1..=m {
            for j in 1..=n {
                if p[j - 1] == b'.' || p[j - 1] == s[i - 1] {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if p[j - 1] == b'*' && j >= 2 {
                    dp[i][j] = dp[i][j - 2]
                        || ((p[j - 2] == b'.' || p[j - 2] == s[i - 1]) && dp[i - 1][j]);
                }
            }
        }

        dp[m][n]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example1() {
        let s = "aa".to_string();
        let p = "a".to_string();
        assert_eq!(Solution::is_match(s, p), false);
    }

    #[test]
    fn test_example2() {
        let s = "aa".to_string();
        let p = "a*".to_string();
        assert_eq!(Solution::is_match(s, p), true);
    }

    #[test]
    fn test_example3() {
        let s = "ab".to_string();
        let p = ".*".to_string();
        assert_eq!(Solution::is_match(s, p), true);
    }
}
