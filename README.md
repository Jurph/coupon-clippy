# coupon-clippy
An AI/ML assistant to parse grocery store flyers and generate bargain-hunting shopping lists

# Vision & Mission 

A digital assistant who can answer questions like: 
- "I'm going to the Giant, are there good prices on anything I can freeze?"
- "I'm making a batch of gumbo, which store should I go to?"
- "Here's this week's shopping list, can you split it across the Giant on Sanner and the Wegman's in Columbia for best savings?" 

# TODO
- Set up LLM-based multi-agent system framework
- Agents should include PDF parser agent, pricing DB manager agent, and a 'bargain hunter' agent, maybe a scraper agent 
- PARSER AGENT: Parse static PDFs to "item short name, item detailed description, price" structure
- SCRAPER TOOL: Scrape local grocery website(s) if possible to automatically get PDFs (this appears well defended against exactly my plan!) 
- Build a pricing database that stores item/date/price tuples to identify what a "good price" is
- Eventually "age out" data and store prices in one-month bins with high/median/low 
- Store my asserted good prices ('bargains.txt') 
- Use local or SaaS LLM agents to process the data more simply
- Provide a simple (streamlit?) web app on local network so anyone on my LAN can ask questions

