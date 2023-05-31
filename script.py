import json

data = [
    {
        "Artist": "Dan Seagrave",
        "Style": "Graphic Realism",
        "Medium": "VHS",
        "Genre": "deathcore",
        "Color Scheme": "RGB",
        "Art Theme": "Ancient Art",
        "Symbolism": "Symbolism",
        "Lighting Technique": "Shadows and Contrast Lighting",
        "View Angle": "Top view"
    },
    {
        "Artist": "Travis Smith",
        "Style": "Grim Impressionism",
        "Medium": "Noise",
        "Genre": "doomcore",
        "Color Scheme": "Pastel colors",
        "Art Theme": "Comics",
        "Symbolism": "Occultism",
        "Lighting Technique": "Spotlight",
        "View Angle": "Low Angle"
    },
    {
        "Artist": "Arik Roper",
        "Style": "Fantastic Realism",
        "Medium": "Ink Drops",
        "Genre": "symbolic",
        "Color Scheme": "Triangular scheme",
        "Art Theme": "Concept Art",
        "Symbolism": "Magick",
        "Lighting Technique": "Diffuse lighting",
        "View Angle": "High angle"
    },
    {
        "Artist": "David V. D'Andrea",
        "Style": "Technical Drawing",
        "Medium": "Scuffs",
        "Genre": "technoshamanism",
        "Color Scheme": "Complementary colors",
        "Art Theme": "Devil's Style",
        "Symbolism": "Rituals",
        "Lighting Technique": "Dimming and Semi-darkening",
        "View Angle": "Close-up"
    },
    {
        "Artist": "Tony Roberts",
        "Style": "Photorealism",
        "Medium": "Glitch",
        "Genre": "Horrorcore",
        "Color Scheme": "16 bit color scheme",
        "Art Theme": "Dune",
        "Symbolism": "Witchcraft",
        "Lighting Technique": "Silhouette lighting",
        "View Angle": "Back view"
    },
    {
        "Artist": "Andreas Marschall",
        "Style": "Mystical minimalism",
        "Medium": "Color filters",
        "Genre": "Hellcore",
        "Color Scheme": "Analog",
        "Art Theme": "Pixel Art",
        "Symbolism": "Shamanism",
        "Lighting Technique": "Glare and transmitted light",
        "View Angle": "Side view"
    },
    {
        "Artist": "Gyula Havancsák",
        "Style": "Digital Illustration with Effects",
        "Medium": "Graphic Noise",
        "Genre": "Gothic culture",
        "Color Scheme": "Separation Scheme",
        "Art Theme": "Technological style",
        "Symbolism": "Esotericism",
        "Lighting Technique": "Contrasting colors",
        "View Angle": "First person view"
    },
    {
        "Artist": "Eliran Kantor",
        "Style": "Oil Painting",
        "Medium": "Highlights",
        "Genre": "Horror fiction",
        "Color Scheme": "Tetradic scheme",
        "Art Theme": "Oil Painting",
        "Symbolism": "Dark",
        "Lighting Technique": "Poorly lit backgrounds",
        "View Angle": "Third-person view"
    },
    {
        "Artist": "Android Jones",
        "Style": "Digital Realism",
        "Medium": "Blur",
        "Genre": "Dark art",
        "Color Scheme": "Mixing scheme",
        "Art Theme": "",
        "Symbolism": "macabre",
        "Lighting Technique": "Pulsating lighting",
        "View Angle": "Panoramic view"
    },
    {
        "Artist": "Simon Haiduk",
        "Style": "Photorealistic Digital Painting",
        "Medium": "Speckle Noise",
        "Genre": "Supernatural",
        "Color Scheme": "Acromatic scheme",
        "Art Theme": "",
        "Symbolism": "",
        "Lighting Technique": "Dim lighting and backlighting",
        "View Angle": "Forced perspective"
    }
]

json_data = json.dumps(data, indent=4)

with open('data.json', 'w') as json_file:
    json_file.write(json_data)
