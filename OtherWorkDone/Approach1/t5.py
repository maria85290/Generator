from transformers import pipeline

# using pipeline API for summarization task
summarization = pipeline("summarization")
original_text = "Does Shaking Duvets Increase Heart Attack Risk?ITV News reported on a recent study that found people who vigorously shake their duvets are at an increased risk of heart attacks.These posts falsely argued that the media was attempting to disguise an increased risk of heart attacks from the COVID-19 vaccine by publishing a wave of articles blaming other factors (such as rigorously shaking a duvet cover) for heart attacks.First, articles and studies about heart attack risk are not unique to the pandemic.More importantly, studies have found that there is a higher risk of heart attacks from COVID-19 itself than there is from the vaccine. Sudden death in COVID-19 patients caused by arrhythmia can be a consequence of these heart problems […] Rare heart inflammation cases (around one in 6000) were reported in teenagers after their COVID-19 vaccination."
summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)