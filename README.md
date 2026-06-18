# Supply Chain Analytics Dashboard



#### Why I Built This



I started this project because I kept seeing the same problem across supply chains: companies collect tons of data but rarely use it to actually improve operations. They know shipments are late, but they don't know why or where to fix it. Data sits in spreadsheets while decisions get made on gut feel.



This project is my way of showing how to change that. I wanted to take a real supply chain dataset and build something that doesn't just report numbers—it tells a story about what's actually happening and why it matters.



#### The Problem We're Solving



Imagine you're running a global logistics operation. You have orders coming in from everywhere, going everywhere, with different shipping modes and customer expectations. Some orders get delivered on time; others don't. Some are profitable; others barely make money. You have hundreds of suppliers, thousands of SKUs, and regions with wildly different performance.



\-The question isn't whether you have a supply chain problem. It's: where exactly is it, how big is it, and what do you do about it?



That's what this analysis answers.



#### What I Analyzed



I worked with a real dataset of 180,519 orders from a global company. That's not a toy dataset—it's messy, it's complex, and it has real business consequences embedded in it.



##### Key Findings



Only 42.72% of orders arrive on time. That means almost 6 out of 10 orders are late. If you're a customer, that's frustrating. If you're the company, that's a reputation problem and a cost problem.



54.83% of orders carry late delivery risk. That's not random variation—it's a pattern. It says something is structurally wrong with either your suppliers, your forecasting, or your routing decisions.



You're generating $36.78M in sales across these shipments, but only keeping $3.97M in profit. That 12% profit margin is meaningful, but it also means you're vulnerable. Small inefficiencies compound.



The interesting part is that performance varies wildly by market, by product category, by shipping mode. It's not a company-wide problem—it's specific problems in specific places.



#### What I Actually Did



Here's the process, because I think it matters:



**Step 1**: Getting the Data Clean



Raw supply chain data is never clean. It comes with encoding issues (especially with international names and addresses), inconsistent date formats, missing values in key fields. I handled all that—parsed dates properly, dealt with character encoding, validated the data. This is the unsexy part of analytics that actually determines whether your results are trustworthy.



**Step 2**: Asking the Right Questions



Instead of just calculating averages, I broke things down by dimensions that actually matter for decision-making:



\- How does each shipping mode perform on cost, speed, and reliability?

\- Which product categories are driving profit? What are the problem areas?

\- Do different customer segments have different needs and behaviors?

\- How consistent is performance across different markets?



**Step 3**: Calculating Metrics That Matter



Every metric in this analysis answers a business question:



\- On-time delivery rate tells you about the service level

\- Late delivery risk shows vulnerability

\- Profit by category tells you where to focus

\- Cost per shipment by mode tells you about efficiency



**Step 4**: Structured Output



I didn't dump everything into one Excel sheet. The output is organized into separate views—summary metrics, shipping analysis, delivery status breakdown, category performance, segment analysis, market performance. Each tells part of the story. This structure makes it easy to build a Power BI dashboard or dig deeper.



#### The Numbers



Here's what the data shows:



**Orders analyzed**: 180,519 (large enough to show real patterns, not noise)



**On-time delivery**: 42.72% (industry standard is 95%+, so this is a huge gap)



**Late delivery risk**: 54.83% (more than half your orders are at risk, that's the main problem)



**Sales volume**: $36.78M (scale of operations, this is significant)



**Profit:** $3.97M (what you're actually keeping after all costs)



**Average delivery time:** 3.5 days (tells you about operational efficiency)



\-The story these numbers tell: you have a significant delivery performance problem that's costing you. Not in a catastrophic way, but in a way that compounds—customer dissatisfaction, potential penalties, reputation damage, and lost repeat business.



#### How I Built It



###### The Tools



Python for the heavy lifting, Pandas for data manipulation, Excel output so it works with Power BI and business teams.



###### The Pipeline



Raw CSV comes in, I handle encoding and date parsing, calculate the metrics by business dimensions, then export to a structured Excel file with multiple sheets.



###### The Technical Approach



I calculated on-time delivery as a binary (real days vs scheduled days), assessed late delivery risk from the dataset, and built summary tables grouped by shipping mode, product category, customer segment, and market. Each aggregation is clean and queryable.



#### Why This Approach Works



A lot of supply chain analysis stays in dashboards and reports that nobody really uses. I wanted to build something different—something that shows actual business thinking, not just data manipulation.



That means starting with real problems (not made-up metrics), analyzing data at the granularity that matters for decisions, structuring output so it's easy to act on, and being honest about what the data shows. Late delivery is a real problem here, not something to spin.



#### What's Next



The natural next step is a Power BI dashboard. I'm thinking of an interactive geographic heatmap of delivery performance, drill-down by supplier and shipping mode, profit and margin analysis by product, customer segment behavior and value, and late delivery risk forecasting.



But the foundation is solid. The data is clean, the metrics are calculated, and the structure is ready.



#### Technical Stack



Python 3.12, Pandas, NumPy, openpyxl. Nothing fancy, nothing overcomplicated. Just the right tools for the job.



###### How to Run This



Clone the repo, install requirements, run the pipeline:



```bash

git clone https://github.com/Tiyyali/supply-chain-analytics-dashboard.git

cd supply-chain-analytics-dashboard

pip install -r requirements.txt

python src/data\_pipeline.py

```



Output shows up in output/supply\_chain\_analysis.xlsx with all the analysis broken down.



#### What I Learned Building This



Data quality matters more than you think. Spending time on encoding, date parsing, and null handling feels boring, but it's what determines whether your results are trustworthy.



Context is everything. A 42% on-time delivery rate is meaningless unless you know what it should be. That's why understanding the business is as important as understanding the data.



Simple is usually better. I could've built a complex machine learning model, but the real insight is just looking at the data carefully and asking what's actually going wrong.



Metrics need to drive decisions. If you're calculating something, it should be something someone can actually act on.

License
---



This project is licensed under the MIT License — see the \[LICENSE](LICENSE) file for details.



\---



#### Author



Meghana Tiyyali  

Supply Chain Optimization | Business Analyst | Data Analyst 

meghanatiyyali0901@gmail.com 

\[GitHub](https://github.com/Tiyyali)





#### 

