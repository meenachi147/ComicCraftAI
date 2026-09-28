def generate_image(prompt, panel_number):

    final_prompt = f"""
    Comic book illustration.
    High quality.
    Detailed composition.
    Clear main character.
    Expressive face.
    Consistent comic art style.
    Strong visual storytelling.
    No text inside the image.

    {prompt}
    """

    print(f"Generating image for panel {panel_number}...")
    print(f"Using model: {MODEL_NAME}")

    try:
        image = client.text_to_image(
            prompt=final_prompt,
            model=MODEL_NAME
        )

        filename = f"panel_{panel_number}.png"

        filepath = os.path.join(
            OUTPUT_DIR,
            filename
        )

        image.save(filepath)

        print(f"Panel {panel_number} saved:")
        print(filepath)

        return "/static/panels/" + filename

    except Exception as e:
        print("========== IMAGE GENERATION ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        print("============================================")
        raise