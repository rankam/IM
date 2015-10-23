## Database/Application Design Problem

### Questions
1. Can a new third party data provider be added easily?

	I think a simple solution, to avoid having to add columns to existing tables, would be to create an additional table, Data_Providers, that includes the data (and hence the columns with the addition of a primary key) that are in the files that are stored in the Google Cloud Storage Bucket. You could then create a table view that consists of at least Campaign_id, Media_cost, Data_cost, Cost_to_Client, Cost_to_Client_with_Data and then any other data necessary (such as date). The Data_cost would be calculated by joining the Delivery_by_day table with the Data_Providers table on the Campaign_id, using a case statement on the Metric_charged column in the Data_providers column to decide if it's CPC or Revenue share - if it's CPC, multiple the rate_paid_to_third_party by the clicks column and if it's Revenue Share, multiply rate_paid_to_third_party by Media_cost. You could then apply this same logic to rate_charged_to_client column and add that number to Cost_to_client to get the Cost_to_Client_with_Data. If you are using Postgres 9.3+, it is possible to create a view that is automatically updated when the data in the related tables is changed, or you could write a function to automatically update the view once per day if you want to avoid the view updating many times per day (assuming that the data in the other table changes multiple times per day) or if the database does not include the functionality to automatically update the view (I'm not sure if MySQL has this functionality).

2. How easily can we measure the impact of these additional costs on the profitability of
campaigns? Profitability is defined as profit/cost to client. Profit is defined as cost to
client – data costs – media costs.

	Using my solution above, this could be easily done by adding a Profitability column which is (cost to client – data costs – media costs) / cost to client. 

3. Is there a way to record when people make changes so that we can trace when costs
change?

	You could include a timestamp column in the Data_Providers table that updates any time a change is made or you could specify that it only updates when columns relating to costs change. 