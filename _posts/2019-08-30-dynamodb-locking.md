---
layout: post
title: DynamoDB Transactions
subtitle: Now Offering Atomic Guarantees and ACID Compliance
css: css/prt.css
---

DynamoDB wasn't designed with ACID compliance in mind. When creating a new tool, you don't want to reinvent the wheel. In fact, that wouldn't be creation at all.  Dynamo was meant to offer low overhead, highly scalable, durable, and eventually consistent storage.  It did what it was designed to do well: offer a data store for the age of agile methodology. Sometimes though, data storage infrastructure will confer outcomes down the line that architects don't design for. Moving all of a team's data, let alone an entire company's, to a new and better designed storage solution is costly both in term of time and opportunity cost.  
 As such, providers of architecture and data storage solutions, so common in the age of agility and cloud computing, find great benefit in empowering their customers through designing for what they need, either now or inevitably.  In the case of transactions, a lot of back and forth between the developer community and the aws teams seems to have taken place.  This is a good thing, and paying attention to customer-created solutions will empower more customers facing similar issues.  AWS ended up creating a solution server-side, which made the API cleaner and more pleasant to use.  
  Transactions offer the abiliy to lock one or more tables in the same "transaction", ie collection of datastore updates, granted they belong to the same storage instance. DynamoDB uses JSON representations to agnosticize the data being stored. The different language clients have defined ways of moving from the JSON representation to the language and preferred representation of their stored objects.  The JSON representation of the payload matters, as DynamoDB has a DSL termed "expressions" which allow for querying and condition checking and updating, amongst other things.    What this is used for, is an intermediary language to handle the RESTful behaviors we all know and love.  
  A payload to update dynamo might look like this:













```JSON
{
	"TableName": "Customer",
	"Key":{
		"CustomerNumber":{"D":5567},
		},
	"UpdateExpression":"SET purchasePredictionCorrect = :purchased_predicted_item, lastPurchaseTime = :most_recent_purchase",
	"ConditionExpression" : "status= :expected_status",
    "ExpressionAttributeValues":
		{":expected_status={D:target_demographic,},
			:purchase_update={S:true,},
			:lastPurchaseTime={S:2019-08-26T12:35:25,}"},
}
```
