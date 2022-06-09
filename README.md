Create a Scrapy spider, that takes an arbitrary single product URL from www.target.com as command line argument, 
e.g. scrapy crawl target -a url=...

Sample URLs - 
https://www.target.com/p/-/A-81260450
https://www.target.com/p/-/A-13493042
https://www.target.com/p/-/A-78299890


{'url': 'https://www.target.com/p/-/A-81260450',
 'title': 'Seventh Generation Fabric Sheets - Morning Meadow - 80ct',
  'description': 'Seventh Generation Dryer sheets Morning Meadow scented leave your clothes', 
  'currency': '5',
   'price': '$',
    'ingredients': [], 
	'specs': "Specifications\nScent: 
	Fresh, Meadow\nHealth Facts: Artificial Fragrance-Free, Phosphate-Free, Contains Naturally Derived Ingredients,
	 Animal By-Product-Free, Hypoallergenic\nProduct Warning: Keep out of reach of children, flush immediately 
	 if product enters eyes, keep out of reach of animals, drink water if product is swallowed\nProduct Form: Sheet\nSustainability Claims: Plant-Based, Cruelty-Free, Not Tested on Animals\nPackage Quantity: 80\nIndustry or Government Certifications: USDA Certified Biobased Product\nTCIN: 81260450\nUPC: 732913448340\nItem Number (DPCI): 003-02-0383\nOrigin: Made in the USA and Imported\nGeneral Disclaimer:\nContent on this site is for reference purposes only. Target does not represent or warrant that the nutrition, ingredient, allergen and other product information on our Web or Mobile sites are accurate or complete, since this information comes from the product manufacturers. On occasion, manufacturers may improve or change their product formulas and update their labels. We recommend that you do not rely solely on the information presented on our Web or Mobile sites and that you review the product's label or contact the manufacturer directly if you have specific product concerns or questions. If you have specific healthcare concerns or questions about the products displayed, please contact your licensed healthcare professional for advice or answers.", 'tcin': 'TCIN: 81260450', 'upc': 'UPC: 732913448340'}

The code is expected to return the output for sample URL in below format :

{
    "url": "https://www.target.com/p/seventh-generation-fabric-sheets-morning-meadow-80ct/-/A-81260450",
    "tcin": "81260450",
    "upc": "732913448340",
    "price": 5.99,
    "currency": "USD",
    "title": "Seventh Generation Fabric Sheets - Morning Meadow - 80ct",
    "description": "Read reviews and buy Seventh Generation Fabric Sheets - Morning Meadow - 80ct at Target. Choose from contactless Same Day Delivery, Drive Up and more.",
    "specs": null,
    "ingredients": [
			"C16-18 glycerides (plant-derived softener)",
			"di-(palm carboxyethyl) hydroxyethyl methylammonium methyl sulfates (plant-based softener)",
			"C16-18 fatty acids (plant-derived softener)",
			"plant-derived fragrances: pogostemon cablin (patchouli) oil",
			"litsea cubeba fruit oil",
			"citrus aurantium bergamia (bergamot) fruit oil",
			"juniperus mexicana (cedar) oil",
			"linalool",
			"cananga odorata (ylang ylang) flower oil",
			"geraniol",
			"citrus aurantium dulcis (orange) peel oil",
			"eugenia caryophyllus (clove) leaf oil",
			"ethyl hexanoate",
			"coriandrum sativum (coriander) fruit oil",
			"heliotropine",
			"styrax tonkinensis resin extract",
			"gamma-nonalactone",
			"phenethyl alcohol",
			"pelargonium graveolens (geranium) flower oil",
			"eugenia caryophyllus (clove) bud oil",
			"juniperus virginiana (cedar) oil",
			"cistus ladaniferus resin",
			"bulnesia sarmientoi (guaiacwood) oil",
			"citrus limon (lemon) peel oil",
			"citrus grandis (grapefruit) peel oil",
			"illicium verum (anise) fruit/seed oil",
			"lauraldehyde",
			"eugenol",
			"citrus nobilis (mandarin orange) peel oil",
			"citrus aurantium amara (bitter orange) leaf/twig oil",
			"cinnamomum zeylanicum (cinnamon) leaf oil",
			"citrus aurantifolia (lime) oil",
			"boswellia carterii oil",
			"vanillin",
			"3-hexenol",
			"abies sibirica (pine) needle oil",
			"eucalyptus citriodora oil",
			"daucus carota sativa (carrot) seed oil",
			"elettaria cardamomum (cardamom) seed oil",
			"gamma-undecalactone",
			"mentha arvensis (mint) leaf oil",
			"salvia sclarea (clary sage) oil",
			"benzyl acetate",
			"gaultheria procumbens (wintergreen) leaf oil",
			"methyl cinnamate",
			"octanal",
			"cinnamomum camphora (camphor) bark oil",
			"ethyl butyrate",
			"artemisia pallens (davana) flower oil",
			"rosa damascena (rose) flower oil",
			"citrus aurantium dulcis (orange) flower oil",
			"decanal",
			"*Safe when used as directed"
	]
    }
}