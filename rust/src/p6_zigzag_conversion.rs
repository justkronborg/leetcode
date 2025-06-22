pub struct Solution;

impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 || num_rows as usize >= s.len() {
            return s;
        }
        let mut rows = vec![String::new(); num_rows as usize];
        let mut curr_row = 0;
        let mut going_down = false;

        for c in s.chars() {
            rows[curr_row].push(c);
            if curr_row == 0 || curr_row == (num_rows as usize - 1) {
                going_down = !going_down;
            }
            if going_down {
                curr_row += 1;
            } else {
                curr_row -= 1;
            }
        }

        rows.concat()
    }
}