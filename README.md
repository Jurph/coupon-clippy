# coupon-clippy
An AI/ML assistant to parse grocery store flyers and generate bargain-hunting shopping lists

# Vision & Mission 

A digital assistant who can answer questions like: 
- "I'm going to the Giant, are there good prices on anything I can freeze?"
- "I'm making a batch of gumbo, which store should I go to?"
- "Here's this week's shopping list, can you split it across the Giant on Sanner and the Wegman's in Columbia for best savings?" 

# Setup and Configuration

## Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/coupon-clippy.git
cd coupon-clippy
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ENVIRONMENT=development
     ```

   You can get an OpenAI API key by:
   1. Going to https://platform.openai.com/
   2. Creating an account or signing in
   3. Navigating to API Keys in your account settings
   4. Creating a new secret key

   Note: Never commit your `.env` file to version control. The `.gitignore` file is configured to prevent this.

## Running the Application

1. Activate your virtual environment if you haven't already:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the example script:
```bash
python src/example.py
```

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

# Architecture 

An adaptible multi-agent system (MAS) that can accommodate new advances in LLMs and tool-using agents. Each tool should be callable via a FastAPI wrapper with documentation, so that an LLM can read the documentation for the API and effectively use the tool by making API calls. The LLM agent should be able to announce to a Project Manager agent what capabilities it has ("I can extract prices from a grocery store's PDF"). Each spot in the system requiring an LLM agent should be able to call a local Ollama model or, given API keys, a frontier model like Claude or ChatGPT, so there probably needs to be a model configuration file which is **not** pushed to the repository. 

