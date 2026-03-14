import streamlit as st
from news_fetcher import fetch_news, combine_articles
from ai_generator import generate_news
from publisher import post_to_discord

st.set_page_config(page_title="AI News Generator", layout="centered")

st.title("AI News Generator → Discord Publisher")

topic = st.text_input("Enter News Topic", "Artificial Intelligence")
word_limit = st.slider("Article Word Limit", 50, 500, 150)

generated_article = None

if st.button("Generate News"):

    with st.spinner("Fetching latest news..."):
        articles = fetch_news(topic, max_articles=5)

    if not articles:
        st.warning("No articles found.")
    else:
        source_text = combine_articles(articles)

        with st.spinner("Generating AI article..."):
            generated_article = generate_news(source_text, topic, word_limit)

        st.subheader("Generated Article")
        st.write(generated_article)

        st.session_state["article"] = generated_article


if "article" in st.session_state:

    if st.button("Publish to Discord"):

        success = post_to_discord(st.session_state["article"])

        if success:
            st.success("Article successfully published to Discord!")
        else:
            st.error("Failed to publish article.")
