use std::collections::HashMap;

impl Solution {
    pub fn max_score_words(words: Vec<String>, letters: Vec<char>, score: Vec<i32>) -> i32 {
        let mut letter_counts = HashMap::new();
        for &letter in &letters {
            *letter_counts.entry(letter).or_insert(0) += 1;
        }

        fn backtrack(
            start_index: usize,
            words: &Vec<String>,
            letter_counts: &HashMap<char, i32>,
            score: &Vec<i32>,
            current_score: i32,
        ) -> i32 {
            let mut max_score = current_score;
            for i in start_index..words.len() {
                let mut new_counts = letter_counts.clone();
                let mut valid_word = true;
                let mut word_score = 0;

                for &letter in words[i].as_bytes() {
                    let count = new_counts.entry(letter as char).or_insert(0);
                    *count -= 1;
                    if *count < 0 {
                        valid_word = false;
                        break;
                    }
                    word_score += score[(letter - b'a') as usize];
                }

                if valid_word {
                    max_score = max_score.max(backtrack(
                        i + 1,
                        words,
                        &new_counts,
                        score,
                        current_score + word_score,
                    ));
                }
            }
            max_score
        }

        backtrack(0, &words, &letter_counts, &score, 0)
    }
}