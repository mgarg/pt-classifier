# Title Cluster Labeling Prompts

## System Prompt

You are an ecommerce taxonomy expert.
Your task is to label product clusters using representative product titles.
Return concise, shopper-friendly taxonomy labels.

## Cluster 0

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 0
Cluster size: 377

Representative product titles:
1. [All Beauty] (3 Pack) RIMMEL LONDON Brow This Way Eyebrow Gel - Medium Brown
2. [All Beauty] (6 Pack) NYC HD Automatic Eyeliner - Deep Brown
3. [All Beauty] (6 Pack) NYC Waterproof Eyeliner Pencil - Black
4. [All Beauty] 1+1 Mascara Applicator Guide Tool Mascara Shield Eyeliner Guide Template Eye Makeup Tool
5. [All Beauty] 100 Glue Holder Rings Cup 100 Eyeliner Brushes Eyelash Mascara Wands and 100 Lipstick Brush Gloss Wands Applicator
6. [All Beauty] 10Pcs Paint Eyebrow Pencil Set Enhancer Makeup Tools Drawing Eye Brow Pen Pencil Cosmetic Eye Permanent Make up Definer Eyebrow Shaping Stencil Template Razor Trimmer Microblading Pencils
7. [All Beauty] 12pcs Zhalya Full Makeup Brushes Set with Large Size Foundation Brush, Blending Face Powder, Blusher, Concealer, Eyeliner, Eyeshadow Brush, Comes with PU Leather Bag for Storage.
8. [All Beauty] 2 Colors Natural Freckle Pen, Faux Lifelike Freckle Makeup Pen Magic Freckle Color, Waterproof Long Lasting Soft Dot Spot Pen for Natural Effortless Makeup (soft brown+dark brown)
9. [All Beauty] 2 In 1 Lipstick Pen, Women Lip Liner Double End Head Lasting Lip Liner Stick Pencil Lipstick 8 Colors Available (H)
10. [All Beauty] 2 Pack Palladio Beauty Retractable Eye Liner Pencil 02 Black Brown
11. [All Beauty] 4 Point Eyebrow Pen, Micro Ink Brow Pen Waterproof Eyebrow Pencil With Micro-Fork Tips for Daily Natural Eye Brown Makeup
12. [All Beauty] 8 Sheets 78 Pairs 4D Hair-like Authentic Eyebrows Waterproof Natural Eyebrow Tattoo Stickers False Eyebrows Grooming Shaping Brow Shaper Makeup, 8 Styles
13. [All Beauty] Anmor 29PCS Makeup Brushes Foundation Brush Make Up Brushes Soft Synthetic Powder Contour Eyeshadow Eyebrow pinceaux maquillage
14. [All Beauty] Avon Glimmersticks Chromes Eye Liner - Veluxe Blue
15. [All Beauty] BallHull 300 Pcs Mascara Wands Applicator Disposable Eyelash Makeup Brush for Eyelash Extension Eyebrow and Brow Definer, Black
16. [All Beauty] Buytra 20-Piece Makeup Brushes Makeup Brush Set Cosmetics Foundation Blending Blush Eyeliner Concealer Face Powder Brush
17. [All Beauty] CCbeauty 6-Packs Double Ended Spoolie and Angled Eyebrow Brushes Set Makup Eyebrow Kit and Eyebrow Comb for Application of Brow Powders Waxes Gels and Blends (#3)
18. [All Beauty] CHENGYIDA 5-PACK (12F needles) Disposable Permanent Eyebrows Makeup Manual Pen Blade
19. [All Beauty] Color Permanent Makeup Ink Black .5 Ounces
20. [All Beauty] Crazy K&A Cosmetic Makeup 12 Colors Waterproof Eyeliner Eyeshadow Pen Set (#2)
21. [All Beauty] EM Cosmetics Fine Liner Brunette Brow Pencil By Michelle Phan
22. [All Beauty] Eyebrow Gel By FLOWER Beauty | FIBER FIX BROW GEL | Tinted Brow Mascara & Fixative for Eyebrows | Vegan & Cruelty-Free | Color: Blonde
23. [All Beauty] Eyebrow Pen,Eyebrow Pencil with a Micro-Fork Tip Applicator,Long Lasting,Creates Natural Brows Makeup Effortlessly 1PCS (1#light brown)
24. [All Beauty] Eyebrow Pencil - MoonKong Microblading Brow Pen with a Micro-Fork Tip Applicator, Waterproof Brow Pen for Natural Eye Brown Makeup
25. [All Beauty] FINEJO Women's Makeup Cosmetics Tools Set 15 Colors Creamy Concealer Kit and 1 Brush
26. [All Beauty] Fifth & Skin (ESPRESSO) Natural Water Resistant Brow Powder – EYEBROW SHAPER – EYEBROW FILLER - Talc free – organic - made in usa
27. [All Beauty] Fill And Detail Brows , Waterproof Eyebrow Pomade(BLONDE)
28. [All Beauty] Flutesan Makeup Practice Board Silicone Makeup Practice Face Eye Bionic Skin Makeup Board with 12 Pcs Eyeshadow Brush (Fresh Style), Gold
29. [All Beauty] JASSINS 12 Models Eyebrow Stencil Guide Card Multiple Shapes Eyebrow Template DIY Shaping Makeup Tools
30. [All Beauty] JSDOIN Makeup Brushes Makeup 14 PCs Makeup Brush Set Premium Synthetic Kabuki Foundation Face Powder Blush Eyeshadow Brushes, Rose Golden
31. [All Beauty] Long-Lasting Smudgy-Style Eyeliner Pencil - Alexis Vogel Pudgy Pencil - 3 Colors Available - Create Smoky Eye Looks with Ease - Precise Application - Created by Celebrity Makeup Artist
32. [All Beauty] Makeup Peel-off Eyebrow Gel Tattoo Waterproof Long Lasting Eyebrow Color Beauty . (Gray-black)
33. [All Beauty] Mini 12 Liquid Glitter Eyeliner Stick Set Colors Glitter Eyeshadow Sticks Long Lasting Waterproof Shimmer Eyeshadow
34. [All Beauty] Mynena Clear Eyeliner Eyelash Glue Pen
35. [All Beauty] Nars Velvet Eyeliner - London
36. [All Beauty] One Step Eyebrow Stamp Shaping Kit Brow Powder Stamp with 12 Reusable Eyebrow Stencils with Eyebrow Pen Brushes, Long Lasting Waterproof Buildable (Light Brown)
37. [All Beauty] Ownest Liquid Tattoo Eyebrow Pen With Four Tips Brow Pen, Long-lasting Waterproof Brow Gel for Eyes Makeup-BLONDE
38. [All Beauty] PONY EFFECT Eye Stain Slim Liner | 002 Deep Brown | 1.5mm Super Slim Eyeliner | K-Beauty
39. [All Beauty] Permanent Makeup Manual Pen 2 Head Microblading Pen Operate More Easil with the Aluminum Holder at One End Antiskid Misty Eyebrow Microblading Pen
40. [All Beauty] Pure Vie Professional 3 Colors Eyebrow Powder Palette Makeup Contouring Kit for Salon and Daily Use
41. [All Beauty] ROZO Long lasting and Waterproof Professional Makeup Auto Eyebrow Pencil (NO.5 Dark Brown)
42. [All Beauty] Rosette Bamboo Flat Top Kabuki Makeup Brush for Foundation Powder Blush Brush - Buffing, Stippling, Concealer (1Pcs Kabuki-st1)
43. [All Beauty] Susenstone20 pcs/set Makeup Brush Set (Red)
44. [All Beauty] Swan makeup brush set 11pcs eye shadow brush concealer professional makeup brush
45. [All Beauty] TER Masterpiece 3D Eyebrow Tattoo Waterproof, Light Brown + TER I'm Matte Waterproof Pen Liquid Eyeliner, Black by TER Cosmetics
46. [All Beauty] Tools by Profusion Cosmetics Professional Brush Vault
47. [Premium Beauty] Trish McEvoy Intense Gel Eye Liner, Charcoal, 1.2 g / 0.04 oz
48. [All Beauty] WEGOTTABB 6 sheets 6D Hairlike Eyebrow Tattoo Sticker Black Waterproof Grooming Shaping Eyebrow Sticker in Arch Style for Women and Girls,60 pairs (Elegent Styels(QZ))
49. [All Beauty] Waterproof Brow Definer, Pro Pencil, Eyebrow Pencil (Soft Brown)
50. [All Beauty] XICHEN 6 PCS/Color Waterproof Eyebrow Pencil， with eyebrow brush not easy to smudge Ultra-Fine Mechanical Pencil

Return JSON only with this schema:
{
  "cluster_id": 0,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 1

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 1
Cluster size: 260

Representative product titles:
1. [All Beauty] (6 Pack) 8 Oz Plastic Jars with Lids, Clear Plastic Square Jars with Smooth Black Plastic Lids - 70mm - 240mL Volume by Grand Parfums - Empty 8 Oz Jars with Lids
2. [All Beauty] 10 Pcs Silicone Travel Bottles Set, Travel Size Containers, Leak Proof Squeezable Tubes with Keychain and Retractable Badge Holders, Reusable Bottle for Toiletry, Shampoo, Liquid, Cosmetic (1.3 Oz)
3. [All Beauty] 12 Pieces 2 ml Empty Lip Gloss Tubes Containers Clear Refillable Lip Balm Bottle Transparent Lip Gloss Containers Plastic Lip Balm Tube Bottle with Rubber Insert for DIY Lipstick Makeup Cosmetic
4. [All Beauty] 12PCS 15g/15ml/0.5oz Empty Refillable Round Clear Plastic Jars Small Tins Cosmetic Container Pot Storage with Pink Screw Cap Lid for Cream Lotion Lip Balm Ointments Eye Shadow Sample Package
5. [All Beauty] 18 Pieces Empty Travel Size Bottle with Keychain Holder Set, Includes 6 Reusable Refillable Flip Cap Bottle 30 ml, 6 Keychain Holder Pouch, 6 Wristlet Keychain Lanyard for Soap Liquid Toiletry
6. [All Beauty] 2oz / 60ml Glass Spray Bottles for DIY Refill, Essential Oils, Pillow Mists,Fine Mist Spray -3Packs Amber Color
7. [All Beauty] 3 Pack 120ml Color Push Down Empty Bottle Dispenser for Makeup Remover Nail Polish
8. [All Beauty] 30pcs 8ml Mini Clear Soft Empty Lip Gloss Tubes Container, Refillable Empty Lip Balm Tubes, Mini Lip Gloss Containers for Women Girls DIY
9. [All Beauty] 4pack Vacuum Moisturizer Jar, Cream Jar Vacuum Bottle Dispenser, Pump Jars For Lotions And Creams (1 oz*4pack)
10. [All Beauty] 5 New,, White, Empty, 2.5 oz Deodorant Containers with Caps
11. [All Beauty] 6 Pack Clear Plastic Pump Bottle 16oz
12. [All Beauty] 6pcs children's liquid soap container portable empty bottle hand sanitizer holder cartoon 30ml leak proof refillable plastic travel bottle with removable silicone protective cover
13. [All Beauty] AW Rolling 2in1 14x9x29" Silver Aluminum Cosmetic Makeup Artist Train Case Hair Style 38" Lockable Box Travel
14. [All Beauty] BAGNN Makeup Brush Organizer Holder Travel Makeup Brush Bag Clear Cosmetic Brush Storage Fit for Cosmetic Box Artist Pencil case with 12 Slots (Brushes Not included)
15. [All Beauty] BAR5F Curve Mini Spray Bottles, 5 oz. (Pack of 2)
16. [All Beauty] Betsey Johnson Nylon Quilted Bow Train Top Handle Cosmetic Case Holder - Black
17. [All Beauty] Clear 16x8x30 T-shirt Bags (100 Pack) with Crafting Insert - Reusable Retail Shopping Bags
18. [All Beauty] Cosmetic Bags Makeup Case Travel Toiletry Storage Organizer for Women by H&L (Rose)
19. [All Beauty] Fantasia Spritz Super-Hold 12 Ounce Pump Clear (354ml) (3 Pack)
20. [All Beauty] Glass Spray Bottles Empty 16oz Boston Round Bottle Refillable Container for Essential Oils with Funnel Lables Cleaning Products Aromatherapy Lotions Liquid Soaps (BrownSilver)
21. [All Beauty] HDE Personal Travel Shower Organizer Hanging Toiletry Wash Bag Bathroom Tote (Black)
22. [All Beauty] HOYOFO Lace Toiletry Organizer Travel Makeup Cosmetic Bag with Brush Holders,Pink
23. [All Beauty] HOYOFO Travel Makeup Bag for Women Portable Cotton Make Up Pouch with Handle Cosmetic Beauty Bag, Yellow Grid
24. [All Beauty] Houseables Black Jar Container, 4 Oz, 120 ML Gram Capacity, Plastic, BPA Free, Double Wall w/ Removable Inner Liners & Dome Lids for Cosmetic Samples, Cream, Lotion
25. [All Beauty] Ibnotuiy 50PCS Lip Gloss Tubes 15ml Empty Lipgloss Tubes Containers Refillable Clear Squeeze Tubes for Diy Lip Gloss Balm Cosmetic (Gold)
26. [All Beauty] KOLLEE Toiletry Bag Travel Bag with Hanging Hook, Water-resistant Makeup Cosmetic Bag Extra Large Travel Organizer for Accessories, Shampoo, Full Sized Container, Toiletries
27. [All Beauty] Lifestyle Banquet Leather Dopp Kit for Men (Black) | Travel Hygiene Bag with Multiple Compartments for Shaving or Grooming Accessories and Skin Care Products | 5.5 by 9.5 inches
28. [All Beauty] MagJo Naturals Empty Glass Spray bottle 2 pack (BLACK SPRAYER/MIXED BOTTLES)
29. [All Beauty] Mary Kay - Brush Bag - Unfilled
30. [All Beauty] Mens Travel Toiletry Bag Large Toiletries Bag Waterproof Shaving Bag for Men Grooming Bag Weekender Makeup Bag for Travel Wash bag Overnight Cosmetic Bag Large Personalized Shower Organizer Black Bath
31. [All Beauty] Minkissy 100Pcs 10g Empty Lip Tubes Clear Gloss Containers Refill Empty Tubes Soft Lip Balm Tube DIY Cosmetics Gloss
32. [All Beauty] MoYo Natural Labs 8 oz Spray Bottles Fine Mist Empty Travel Containers, BPA Free PET Plastic for Essential Oils and Liquids/Cosmetics (Pack of 2, Blue)
33. [All Beauty] Mr.XZY Unicorn Galaxy Travel Makeup Train Case Makeup Bag Cosmetic Bag with Train Brushes Dividers Adjustable Jewelry Toiletry Portable Make Up Tools 2010078
34. [All Beauty] NOTONEON Makeup Bag Toiletry Kit Organizer Portable&Waterproof Large Cosmetic Pouch Fashion Women Jewelry Bathroom Storage with Zipper&Drawstrings
35. [All Beauty] Press on Nails Packaging Bags Pink 50pcs Empty Holographic Resealable Bag Display Cardstock Handmade DIY Small Business
36. [All Beauty] Pro Sanitize-Hand Sanitize Cleaning Gel - 1PK 8 fl oz Press Cap Bottle
37. [All Beauty] Purell Instant Hand Sanitizer Refills, Unscented, 2000 mL Refill Bags, Case of 4
38. [All Beauty] Schwarzkopf Pumps for Liter Bottles
39. [All Beauty] Seya Beauty Mini Makeup Train Case
40. [All Beauty] Spray Bottle,Fine Mist Mini 60ml/2oz Spray Bottles,Small Reusable Empty Plastic Bottles with Atomizer Pumps 24 pack (Amber)
41. [All Beauty] Spray Bottles
42. [All Beauty] Sprayco Jc 3 Clear Jar With Leakproof Lid, 3 Ounce
43. [All Beauty] StylesILove Barrel Shaped Travel Dresser Makeup Bag Cosmetic Storage Organizer 3-piece Set - 6 Colors (Light Yellow)
44. [All Beauty] TRENDBOX Soap Dispenser Pump Bottles (4 Pack 16oz/500ml) Shampoo Dispenser Empty Plastic Amber Pump Bottles for Essential Oils, Shampoo, Toner, Lotion, Cream, Hand Sanitizer
45. [All Beauty] Teensery 5 Pcs 4ml Empty Clear Mascara Tube Eyelashes Wand Tube Vials Bottle Container With Plug
46. [All Beauty] Toiletry Bag Dopp Kit for Men, SCORLIA Premium Nylon Travel Bathroom and Shower Organizer Waterproof Shaving Bag for Toiletries Accessories, Personal Items - Grey
47. [All Beauty] Travel Toiletry Bag for Men Women Bathroom Shaving Dropp Kit Waterproof Large Organizer Cosmetic Bag (black)
48. [All Beauty] Travel Toiletry Bag for Men and Women, Waterproof Dopp Kit, Hanging Makeup Organizer for Nail Polish, Razor, Toiletries, Makeup, Bathroom
49. [All Beauty] Travel Toothbrush Case - 5 Pack Portable Breathable Toothbrush Holder Plastic Toothbrush Cover Dust-Proof Toothbrush Storage Box for Travel, Business, Home, Camping, School
50. [All Beauty] ZEN Classic Black Makeup Case / Organizer / Cosmetic Case

Return JSON only with this schema:
{
  "cluster_id": 1,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 2

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 2
Cluster size: 797

Representative product titles:
1. [All Beauty] 100PCS Compressed Towel/Magic Wipe Soft Cotton Expandable Just Add Water Blue
2. [All Beauty] 3D Mask Bracket - Increase Breathing Space Help Breathe Smoothly - Mouth and Nose Protection Lipstick - Washable Reusable - 5PCS
3. [All Beauty] 4 Pcs Sparkle Rhinestone Face Cloth Mask For Women, Stylish Glitter Reusable Black Pink Red Blue Breathable Sequin Designer Adjustable Washable Bling Diamond Crystal Masquerade Fancy Beauty Cute
4. [All Beauty] 5 Pack Homehold Unisex Adjustable Anti Dust External Shielding Cloth,Black Cotton For Cycling Camping Travel
5. [All Beauty] Alaska Fishing: DVD & Ultimate Guide! Lake Creek King Salmon Float Trip
6. [All Beauty] Animal Themed Kid's Face_Mask Face Covering Gear Double Fabric Layers Washable Reusable Unicorn, Bear, Kitty, Bunny and More (Pack of 4 Unicorn)
7. [All Beauty] Annie Classic Foam Cushion Rollers #1051, 14 Count Blue Small 5/8 Inch (3 Pack)
8. [All Beauty] Apple DIY Puzzle -3D Crystal Jigsaw Kids Educational Developmental Assembly Model Building Block Decor Christmas Eve Gift Toy Gift
9. [All Beauty] Azure Green RA315 Bollock Athame
10. [All Beauty] Bar5F Cotton Coil 100% Pure, 40 Feet Per Bag, White, 2 Count
11. [All Beauty] Bobbi Boss Swiss Lace front 13x7 - MLF370 Brooklyn
12. [All Beauty] Bundle Monster 3pc Ultra Soft Mixed Design Padded Eye Mask Ear Plug Travel Pouch Sleep Accessories - Set 4
13. [All Beauty] CHOPMALL(TM) Fashion Lady Retro Infinity Black Elephant Anchor Love Lover Strands Suede Rope Bracelet Gift
14. [All Beauty] China Glaze Seahorsin' Around
15. [All Beauty] Cuttlefish IN Space Galaxy Coin Purse
16. [All Beauty] DND Duo 685 Nova Pinky
17. [All Beauty] Dominican Doobie Wrap And Cap
18. [All Beauty] Dr. George's Plaque Blast
19. [All Beauty] ETopLike 5x 1/4" 3/8" Metal Monopod Tripod Mount Screw Convert Adapter Flash Light Stand Spigot Bracket Holder Camera (1/4" to 1/4")
20. [All Beauty] Ear Covers For Shower 100 Pack Clear Disposable Ear Protector Waterproof Elastic Clear Shower Water Covers Caps
21. [All Beauty] Easy lifestyles Crescent-shaped Silicone Push Up Enhance Invisible Bra Self Adhesive Enhancement Enhancer Falsies Swimsuit Bikini Pads
22. [All Beauty] Fing'rs Prints Ghoulish Glam Vampy Vixen
23. [All Beauty] Fishing Knot Puller Rig Making Tool, 12pcs 3 Colors, Tester Tightener for Carp Fishing Terminal Tackles
24. [All Beauty] Focalwanna 5Pcs M-5 Mic Stand Accessory Small Plastic Clip Holder
25. [All Beauty] GEREE DC 12V Waterproof LED Digital Display Voltmeter for Boat Marine Vehicle Motorcycle Truck ATV UTV Car Camper Caravan Green Digital Round Panel (Green)
26. [All Beauty] It's a Wrap (Medium Copper Blonde)
27. [All Beauty] JML Pedi Pro Deluxe
28. [All Beauty] Kosmart - French Made Clawclip"Loving Myself"
29. [All Beauty] Laura Geller Berry Glow Trio - Full Size 3 Piece Set
30. [All Beauty] Lift Nipple Cover+Double Sided Body Tape Silicone Reusable Pasties Lingerie Fashion Adhesive 4 Body Clothing.
31. [All Beauty] Line Free Lift
32. [All Beauty] Logo Silver Shear Collection #212 by Cricket
33. [All Beauty] Mehaz Corn Planer MC0062
34. [All Beauty] Meta Funky 50 pcs Face Cover
35. [All Beauty] Metal .Black Lobster Clasps 0.6 Inches Internal Diameter D Swivel Trigger Clips Eye Hooks Pack of 6
36. [All Beauty] NICKI MINAJ PINK FRIDAY by NICKI MINAJ
37. [All Beauty] Nikki's Magic Wand, Set of 2
38. [All Beauty] Our Time
39. [All Beauty] PURE SILK EDGE LAYING SCARF - Premium 100% Silk Edge Laying Scarves - Manufactured in The USA (Pink)
40. [All Beauty] Pet Shirt Daoroka Small Large Dog Cat Costume Puppy Vest Summer Letter Sweatshirt Girl Boy Pet Clothes Fashion Apparel (XS, Red)
41. [All Beauty] Rock Your Hair Bling it Duo
42. [All Beauty] Rosmall Newtons Cradle Balance Balls Newtons Balls Swing Balls Physics Science Pendulum Ball Desk Table Decor Black Base Small
43. [All Beauty] Sally Hansen Salon Insta Gel Strips Troublemaker and Commander In Chic 16 Strips Each with Dimple Braclet
44. [All Beauty] Sally Hansen Teflon Tuff 2-in-1 Base & Top Coat
45. [All Beauty] Sephora Collection The Vacationer BLACK
46. [All Beauty] Starkey HearClear Wax Trap for Hearing Aids - 12 Packs = 96 Filters!
47. [All Beauty] Unique Fashionable Braided Black Leather Bracelet Bangle With Silver Coloured Tree, Infinity And Love Plate Charms By VAGA
48. [All Beauty] Usstore 1PC Decorative Pillowcases zip Square Cat Dog Cotton Print Throw Pillow Cover Cafe Home Decoration for Living Sofas Beds Room (G)
49. [All Beauty] beyondSTRAIGHT 8 oz
50. [All Beauty] iphone 7 Plus Case,iphone 7 Plus Pikachu Gel Case,MODEFAN Cartoon Figure Soft Silicone Pikachu Yellow Gel Rubber Case Cover Skin for Apple iphone 7 Plus

Return JSON only with this schema:
{
  "cluster_id": 2,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 3

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 3
Cluster size: 1145

Representative product titles:
1. [All Beauty] 100% Remy Human Hair Silk Base Top Hairpieces Replacement Clip in Topper For Women Crown Top Piece Long 16''/16inch #6 Light Brown 30g
2. [All Beauty] 100% Remy Human Hair Silk Base Top Hairpieces Replacement Clip in Topper For Women Crown Top Piece Short 10''/10inch #6 Light Brown 20g
3. [All Beauty] 10A Body Wave Bundles with Frontal Human Hair Bundles with Lace Frontal Brazilian Body Wave Virgin Hair 3 Bundles with 13x4 Ear to Ear Frontal Closure with Baby Hair (18 20 22 and 16)
4. [All Beauty] 16"-22" Tape in Hair Extensions Skin Weft Real Remy Human Hair Straight 20pcs 30g per pack (20"-30g,#6 Light Brown)
5. [All Beauty] 6 Packs Bomb Twist Crochet Hair 14 Inch Pre looped Mini Passion Twist Braiding Hair Spring Twist Crochet Braids Kinky Curly Synthetic Hair Extensions (14 Inch, 1B/Brown)
6. [All Beauty] 7A Grade Ombre Bundles Straight Hair 3 Bundles Ombre Human hair Honey Blonde Wavy Hair Brazilian Remy Hair Human Hair Weave Extensions 2 Tone #1B 27 Color 12 14 16 inch
7. [All Beauty] 9A Body Wave Human Hair Bundles 100% Virgin Brazilian Hair 3 Bundles (26 28 30 Inch) Weave Hair Human Body Wave Bundles Unprocessed Remy Weave Hair Bundles (26 28 30)
8. [All Beauty] ABH AMAZINGBEAUTY Semi-permanent Real Remi-Remy 100 Human Hair Tape in Extensions 50g-20pcs Glue in Skin Weft Tape Attached Invisible Seamless Reusable Beach Blonde-Bleach Blonde Color 613 22 Inch
9. [All Beauty] Beauty Princess 360 Lace Frontal with Bundles 9a Brazilian Body Wave Virgin Hair 3 Bundles with 360 Lace Band Frontal Closure with Bady Hair Natural Color. (22 24 26+20)
10. [All Beauty] Benehair One Piece Clip in Human Hair Extensions 3/4 Head 18 inch Dark Brown Long Straight Remy Hair Skin Weft Clip On Standard Weft for Women Party (18" #2)
11. [All Beauty] Body Wave Clip in Human Hair for Women Natural Black 100% Real Human Hair Extension Clip in Body Wave Hair Pieces Thick Full Hair Clip ins Body Wavy Human Hairpiece 8 Pieces 130 Gram 22 Inch
12. [All Beauty] Brazilian Straight Hair Bundles 100% Human Hair Straight Bundles 10A Unprocessed Virgin Hair Straight Weave Hair Human Bundles (18 20 22)
13. [All Beauty] Crotchet Braids Box Braids Hair Extensions Ombre Black Brown Burgundy Kanekalon Braiding Hair (14inch,1B)
14. [All Beauty] Down Clip in Human Hair 10" Brown
15. [All Beauty] EZ X Rainbow Pre-Stretched Braids 54" (1/50) (PEACOCK)
16. [All Beauty] Eiazalin 10A Brazilian Hair (24 26 28)
17. [All Beauty] Ez Combs Double Stretching Combs, Thick and Thin Hair, New Hair Accessory for Popular Hairstyles (3#)
18. [All Beauty] FeiBin Hair 4"x4" Brazilian Body Wave Lace Closure Bleached Knots Natural Color 100% Virgin Human Hair Closure Free Part Lace Closure (10 Inch)
19. [All Beauty] Freiuoke 8A Brazilian Hair Bundles Human Hair Body Wave Bundles 613 Honey Blonde Human Hair Weave 100% Unprocessed Virgin Hair 3 Bundles Brazilian Body Wave Bundle for Black Woman 14 16 18 Inch
20. [All Beauty] Freyja Hair Brazilian Virgin Hair Human Hair Closure With Baby Hair Deep Wave Top Lace Closure Part 8-20" Naturl Black Bleached Knots (free part 10")
21. [All Beauty] Fshine Balayage Clip in Hair Extensions Real Remy Human Hair Blonde 14Inch 100Gram Remy Hair Extensions Clip in Human Hair Natural Brazilian Double Weft Clip Hair Piece Ash Blonde to Platinum 10Pcs
22. [All Beauty] GUOHUI Butterfly Locs Crochet Hair 18 Inch Natural Black 6 Packs Pre Looped Soft Distressed Faux Locs Braids for Black Women Kids All Handmade New Straight Style (18",27#)
23. [All Beauty] Hair Extensions Clip in Real Human Hair Clip on Remy Hair Extensions for Black Women Balayage Golden Brown with 613 Bleach Blonde Highlights Double Weft Full Head Natural 70g 7pcs 16 Clips 20 Inch
24. [All Beauty] Hairro Ponytail Hair Extensions 14 Inch 105g #27
25. [All Beauty] Honey Brown Pre Stretched Braiding Hair 8 Packs By Leticia
26. [All Beauty] HuoWoc Straight Bundles Black Brazilian Remy Hair Bundle Hair Extensions 100G/Bundle Human Hair 3 Bundle Grade 8A Unprocessed Virgin Hair Bundle 12 14 16 Inch
27. [All Beauty] Kanekalon Jumbo Braiding Hair 5Pcs 100g/Pcs Synthetic Braiding Hair Kanekalon Hair Royal Blue Color Twist Braid Hair Fiber Jumbo Hair Extensions 24inch
28. [All Beauty] LaaVoo 16" Halo on Remy Hair Extensions Real Human Hair Highlighted Balayage Darkest Brown Ombre to Light Brown and Darkest Brown Flip on Straight Hair Extensions 80g Per Package 11inch Width
29. [All Beauty] Loose Deep Wave Human Hair Extentions Brazilian Virgin Hair Loose Deep Bundles Single Bundle One Bundle (10)
30. [All Beauty] MSGEM 9A Kinky Straight Only 1 Bundle Yaki Straight Human Hair 30 Inch for Black Women 100% Unprocessed Human Hair Weave Brazilian Virgin Hair Extensions Natural Color
31. [All Beauty] Ms Sunlight Ponytail Extensions 100% Human Hair Water Wave Wrap Drawstring Ponytail With Clips in Hair Pieces Pony Tail For Black Women (16 inch,Water Wave)
32. [All Beauty] New Bomb Twist Crochet With Curly Hair 6 Packs Boho Hippie Locs More Small Curls River Locs 14 Inch Bohemia Locs Crochet Hair Synthetic Braids Hair Extensions for Women(144Strands, 1B/27#)
33. [All Beauty] NiegMeag 22 24 26 inch Kinky Curly Bundles Human Hair Curly Human Hair 3 Bundles 100% Unprocessed Brazilian Virgin Hair Curly Weave Hair Natural Black Color
34. [All Beauty] Passion Twist Hair 10 Packs Pre-twisted Passion Twist Crochet Hair 18inch Pre-Looped Passion Twists Crochet Braids Bohemian Hair Synthetic Braiding Hair Extension (18inch,1B/30)
35. [All Beauty] RN BEAUTY Ombre Jumbo Braiding Hair Extensions High Temperature Heat Resistant Synthetic Fiber for Twist Braiding Hair Crochet Weave Braid Hair 5 Pieces/lot 24 Inch 2 Tone Color Black/Silver Grey
36. [All Beauty] RUNATURE Sew in Weft Hair Extensions Human Hair Black Sew in Hair Extensions Human Hair 18 Inch 100g Double Wefted Bundles Extensions Real Human Hair Weave Extensions
37. [All Beauty] SARLA Clip in Hair Bangs Fringe Hair Extensions Swept Full Sweeping Side Synthetic Hairpiece Hair Piece For Women Japan High Temperature Fiber(Ash Brown B2#12C)
38. [All Beauty] Seamless Clip in Mini Hairpiecs 4 Inch Down Short Human Hair for Men and Women Adding Volume #2 Dark Brown Clip on Straight Wiglet Hair Filler Extensions
39. [All Beauty] Senegalese Twist Crochet Hair Extensions Black - 32inch 8Packs Synthetic Crochet Braids Pre Looped Crotchet Hair Synthetic Braiding Hair (32 inch, 2#)
40. [All Beauty] Sew in Human Hair Extensions Double Weft Seamless Brazilian Remy Hair Weave Bundles Natural Sew in Real Hair Weft Ash Brown with 2 Tones Blonde Highlights Silky Straight Full Head 120G 24 Inch
41. [All Beauty] Sew in Real Remy Hair 16 Inch Color 10 Fading to 14 100 Gram per Pack Bleached Extensions Colorful Hair Silky Straight Remy Hair Weft
42. [All Beauty] Straight Clip in Hair Extensions for Women140g/6Pcs Full Head 20 Inch #1B Natural Black Hair Extensions Clip in Hair for Black Women Girls Double Weft Synthetic Hair
43. [All Beauty] Sunwell Weave Hair Human Bundles of Brazilian Hair Extensions Human Hair Bundles Kinky Curly Natural Color 8" 10" 12"
44. [All Beauty] Tape in Full Head Hair Extensions 16 Inch Real Human Hair Extensions Tape in 40pcs 100g Seamless Balayage Tape in Hair Extensions #18 Blonde Ombre to #60 Blonde
45. [All Beauty] Tape in Hair Extensions Human Hair Hot Pink Hair Extensions Straight Tape in Colored Hair Extensions Hot Pink Tape in Extensions Remy Skin Weft 25g 16 Inch
46. [All Beauty] Ushine Brazilian Virgin Hair Bundles Wet And Wavy Human Hair 22 20 18 inch Unprocessed Water Wave 3 Bundles Weave Hair Human Bundles Natural Color
47. [All Beauty] WOME Jumbo Braiding Hair 165G Low Temperature Synthetic Fiber Hair 3Pcs Blonde Color Crochet Twist Braids 82" Long Hair Extensions for Woman
48. [All Beauty] YILITE Colorful Tape in Hair Extensions Remy Human Hair 10pcs 20g Yellowish Green Tape Hair 12 inches
49. [All Beauty] You Are My Sunshine My Only Hair Extension 51
50. [All Beauty] iLUU 18inch 80g Grey Silver Fashion Womens Flio in on Hair Extensions Long Curly Wavy Synthetic Haipieces Hidden Fish Line Invisible String Transparent Wire Flip in Hair Extensions for Party GREY

Return JSON only with this schema:
{
  "cluster_id": 3,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 4

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 4
Cluster size: 182

Representative product titles:
1. [All Beauty] 112 Pieces Hair Silicone Curler Rollers Blue and Pink Hair Curlers Rollers Silicone Set Including 56 Pieces Large Size and 56 Pieces Small Size, with a Transparent Zipper Bag
2. [All Beauty] 18Pcs Magic Hair Curlers Spiral Curls No Heat Wave Hair Curler Styling Kits with Styling Hooks, for Most Kinds of Hairstyles 22"(55 cm) Long
3. [All Beauty] 2 in 1 Ionic Hair Straightening Brush for Short Hair, Portable and Dual Voltage for Travel, 30s MCH Rapid Heating ,Anti-Scald and Auto-Off, Best Gift for Family and Friend
4. [All Beauty] 25mm 3 Barrel Curling Iron Wand,Crimper Hair Iron with LCD Temp Display Temp Adjustable,Ceramic Tourmaline Triple Barrels Hair Waver Heat Up Quickly,Beach Waves Curling Iron with Heat Resistant Glove
5. [All Beauty] 31 Pieces Large Silicone Hair Curlers Set, 30 Pack Magic Hair Rollers 1.9 Inch No Clip Silicone Curlers with a Black Storage Bag for Women and Kids (Large)
6. [All Beauty] 45 Pieces Flexible Curling Rods Twist Flexible Rods No Heat Hair Rollers Soft Foam Hair Rods for Women Girls Long, Medium, Short Hair (Pink,1.2 cm Diameter)
7. [All Beauty] 8 Pack Sleep Hair Rollers- Absorbent sleep hair rollers style Curling Apparatus,Curling Drum,Dry Hair Curler,6 Inch Absorbent Heat Free Sleep Nighttime Styler Curlers
8. [All Beauty] 8 Pieces Volume Hair Curler Clip Natural Fluffy Hair Clip Hair Root Curler Roller DIY Curler Fluffy Clamp Roller Hairstyling Clip Styling Tool No Damage and Heat-free Volumized Hairstyle, Purple, Blue
9. [All Beauty] 80pcs Perm Rods Long Cold Wave Rods 6 Size Perm Rod for Natural Hair Jumbo Large Medium Small Hair Roller Curling Rods DIY Hair Curlers for Long Short Hair(Blue+Orange+Beige+Purple+Grey+White)
10. [All Beauty] 80pcs Perm Rods Set Large Medium Size Cold Wave Rods Hair Roller Curler Variety Perm Rods for Natural Hair Perming Rods Hair Curlers for Women Long Short Hair DIY Hairdressing Styling Tools
11. [All Beauty] ANCIRS 2 Pack Heatless Curls Curling Headband for Girls, Sleepytime Overnight Ponytail Hair Curler for Long Hair, Nighttime Lazy Scrunchie Hair Rollers Hairdresser for Women- Pink
12. [All Beauty] Abodhu 32 Pcs Spiral Curls Wave Styles Hair Rollers No Heat Spiral Curls Magic Curler Spiral Styling Kit with Styling Hook for Long Medium Short Hair(30 cm/11.8 inch)
13. [All Beauty] Annie 1-1/2" XL Wire Mesh Hair Rollers - 12 Pcs.
14. [All Beauty] Automatic Curling Iron Corn Perm Splint Curling Iron Salon Hairdressing Curlformers Professional Tools Specially Designed for Women's Hairdressing
15. [All Beauty] Best Ionic Hair Straightener,Professional Ultrasonic Hair Straightener Steam Flat Iron Temperature Adjustable Ceramic Steampod Spray Curling Iron Straightening Brush Travel XX023
16. [All Beauty] Buwico Protective Travel Storage Case for Dyson Airwrap Styler Hair Curler Accessories for Shark Flexstyle, Hard Shell Shockproof Dustproof Organizer for Dyson Airwrap HS01 Complete Styler Hair Styling Set/Shark Flexstyle(Not for New Dyson Airwrap)
17. [All Beauty] Collapsible Hair Diffuser, Universal Blow Dryer Head Attachment -Travel And Easy Storage-Professional Lightweight Foldable Hairstyling Hairdryer Parts -For Natural Wavy Fine Thick Hair D-1.5 to 1.9"
18. [All Beauty] Cordless Hair Curler, Automatic Curling Iron with 6 Adjustable Temperature, Auto Rotating Ceramic Barrel Hair Curler Fast Heating, Portable USB Rechargeable Beach Waves Curling Iron Wand
19. [All Beauty] Cricket Ionic Tourmaline 5200 IT Professional Hair Dryer
20. [All Beauty] DAN Technology Anti-Scald 200℉-500℉ Electric Press Hot Comb for Black Hair, Beard and Wigs, Ceramic Unisex Hair Beard Straightener and Curler, Dual Voltage for Travel, Home and Salon Use
21. [All Beauty] Deep Conditioning Heat Cap Electric Hair Nourishing Steamer Cap For Hair Spa Home Hair Thermal Treatment Beauty Spa US PLUG
22. [All Beauty] Dprofy Magic Hair Spiral Curlers - 28 Pieces Heatless Curlers Styling Kit with 2 Pieces Styling Hooks, for Extra Long Hair Most Kinds of Hairstyles (45 Cm/ 17.7 Inch)
23. [All Beauty] Flat Iron - 2in1 Ceramic Hair Straightener & Curling Iron Wand Dual Voltage Hair Curler Portable Travel 1 Inch Straightening Iron 30s Fast Heat Up w/Adjustable Temperature for All Hair Thick 110-240V
24. [All Beauty] Hair Dryer Brush, Blow Dryer Brush 3-in-1 Hair Dryer and Styler Volumizer with Negative Ionic for Fast Drying, Straightening, Inner Curling, Anti-frizz Hot Air Brush with 3 Adjustment Modes
25. [All Beauty] Hair Rebonding Sofia Professional Hair Straightener (N1) + Neutralizer for Fine or Tinted hair(N2)
26. [All Beauty] Hair Steamer By Skin Act
27. [All Beauty] Hair Straightener Brush, AutoYet2 with 2-in-1 straightening Comb for Straightener and Curly Hair, Anti-Scald Heated Function Fast Heating instyler Rotating Iron for All Hair Types,Black(ATYT300B)
28. [All Beauty] Hair Straightener Irons, Automatic Release Negative Ions, 2 in 1 Twist Straightening Iron hair Curling Iron, 3D Concave and Convex Titanium Plate New Design
29. [All Beauty] Hair Straightener Professional Detangling Hair Brush Hair Styling Comb Digital Anti Static Anti-Scald Ceramic Heating Iron Pink Hair Massage Straightening Irons (White)
30. [All Beauty] HaloVa Hair Dryer Holder, Wall Mount Drill-free Hair Dryer Rack, Multifunctional Premium Hair Blower Storage Organizer for Bathroom Washroom, Silver
31. [All Beauty] Hamnor 24 PCS Hair Rollers 21.6" Wave Styling Kit No Heat Hair Rollers Tool for Long Hair with 3 PCS Wands Easy Operate
32. [All Beauty] Hanaive Non-heat Curling Hair Band Sports Hair Band Wave Style Hair Rollers Heatless Curls Ribbon DIY Hair Styling Rollers Tools Night Sleep Hair Curler Rollers for Women Girls (Classic Pattern)
33. [All Beauty] Heatless Hair Curler Rollers, No Heat Flexible Curling Rods Overnight Sleep Styler for Women Natural Long Hair Silk Ribbon Curls with Soft Hairband Scrunchie Clips Tie Set, Absorbent Formers
34. [All Beauty] Heatless Hair Curlers,No Heat Curls Ribbon with Hair Clips & Scrunchie for Long Hair Sleeping Overnight,Yellow
35. [All Beauty] HerStyler Iron Holder, Pink, 1 ea
36. [All Beauty] HuaShanDa Heatless Curling Rod Headband, Tiktok Hair Curlers for Long Hair, Curler You Can To Sleep In Overnight, No Heat Curls Headband Natural Hair-Gifts Women, Pink, 6 Piece Set
37. [All Beauty] Ionic Hair Straightener Brush, BHY Hair Straightening Brush with Negative Ion, 30s Fast Heat up, LCD Display, Auto-Off & Dual Voltage, Portable Ceramic Straightening Comb for Home and Travel
38. [All Beauty] KIMROO 24 Pcs 45cm/17inch Hair Curlers Styling Kit,Wave Style Hair Rollers No Heat with Styling Hooks for Women Girls Long Hair Styling Tools (45cm)
39. [All Beauty] Mia Bend-a-Bun-Soft Flannel Styling Tool With Bendable Wire-Blonde- 7.25" Long (1pc)
40. [All Beauty] New 4 in 1 Roll on Refillable Depilatory Hot Wax Heater Waxing Hair Removal Cartridge Kit Warmer Salon Tools Machine with 100 PCS Paper Strips , Honey Orange Taste 100g Wax Roller, 110v Us Plug
41. [Premium Beauty] NuMe Classic Curling Wand
42. [All Beauty] Parvella Heatless Curls Hair Curlers For Long Hair, Silk Heatless Curling Rod Headband, No Heat Soft Foam Hair Rollers Sleep, Curling Ribbon Hair Rope for Heatless Curls
43. [All Beauty] Prizm Professional 2 in 1 Nano Hair Straightener (1”), Tourmaline Ceramic Styling Flat Iron with 3D Floating Plates and Adjustable Temperature, Fast Heating-up & Dual Voltage, Rose Gold
44. [All Beauty] Professional Water Steam Hair Straightener Flat Iron Injection Painting 450F Straightening Irons Hair Care Styling Tools，For Argan Oil Hair Treatment Vapor
45. [All Beauty] Roll On Wax Warmer with Double Cartridges, Professional Hair Removal Wax Heaters Hair Roller Epilator Wax Machine - Pink
46. [All Beauty] Steam Flat Iron Hair Straightener for Argan Oil Infusion Treatment,1 Inch Professional Ceramic Hair Straightener with,Repair Hair Damage,Auto Shut-Off and Dual Voltage (Black)
47. [All Beauty] Tru Beauty, 1.25-inch LED Curling Iron with Ceramic Coated Barrel for Women & All Hair Types & Lengths- White
48. [All Beauty] Tuisy Electric Heated Eyelash Curler - Rechargeable Automatic Fast Heated Compact Lash Curler with Comb Long Lasting Fits All Eye Shapes
49. [All Beauty] Universal Hair Diffuser For Curly and Natural Hair, Hair Dryer Diffuser Fits 90% Blow Dryer Nozzle 1.7-2.1 inches
50. [All Beauty] Universal Hair Dryer Diffuser Blow Dryer Hair Diffuser Cover fit for Curly Frizzy Hair Styling Hairdressing Salon Accessory (Black)

Return JSON only with this schema:
{
  "cluster_id": 4,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 5

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 5
Cluster size: 403

Representative product titles:
1. [All Beauty] 7 Wonders Nourishing Leave In Conditioner with Pure Organic Oils of Almond, Marula, Argan, Olive, Macadamia, Coconut & Jojoba 16.9 fl. Oz.
2. [All Beauty] Africa's Best Organics Hair Mayonnaise 15 oz (Pack of 2)
3. [All Beauty] American English Luxury Vegan Haircare"Youth Repair Shampoo" 8 oz
4. [All Beauty] Anthocyanin Hair Manicure Color Second Edition 230g/ 8.1 OZ - Semi Permanent Hair Dye - Tempting Hair Color -UV Protection - Plant Protein (OP01 CORAL PINK)
5. [All Beauty] ApHogee Keratin & Green Tea Shampoo 12oz + Restructurizer 8oz"Set"
6. [All Beauty] As I Am Naturally 8pcs ULTIMATE JUMBO COMBO (Curl Shampoo, Leave-In Conditioner, So Much Moisture, Cocoshea Whip, Cocoshea Spray, Smoothing Gel, Detangling Conditioner and Cocnut CoWash)
7. [All Beauty] Beach Freak by TIGI Bed Head Moisturising Detangler Spray 100ml by TIGI
8. [All Beauty] Color Me Natural, 100% Natural Permanent Hair Color, Dark Brown, 4 oz (115 g), From Aubrey Organics
9. [All Beauty] Color Therapy Conditioner by Biosilk for Unisex - 12 oz Conditioner - (Pack of 3)
10. [All Beauty] Doctor Cabello Ligao De Leche Combo Set - Suero leave-in 8.6oz and shampoo 13.2oz
11. [All Beauty] Dominican Hair Product Capilo Romero (Rosemary) Rinse 16oz
12. [All Beauty] Dove STYLE+care Non-Aerosol Hairspray, Strength & Shine, Extra Hold 9.25 oz
13. [All Beauty] Dove STYLE+care Non-Aerosol Hairspray, Strength & Shine, Extra Hold 9.25 oz (Pack of 4)
14. [All Beauty] Earth Chemistry Volumizing Clay Lavender, Cedarwood & Ylang Ylang Thickening Clay Shampoo & Conditioner Set, Clay Shampoo Concentrate
15. [All Beauty] Elgon Silver Shampoo Color Care 10.14oz 300ml
16. [All Beauty] Fudge Urban Sea Salt Texturizing Spray
17. [All Beauty] Green Pharmacy. Balm Hair conditioner Linden flower and Sea Buckthorn oil. For dry and damaged hair (Липовый цвет и облепиховое масло)
18. [All Beauty] Grow Strong MAFURA - Natural Hair Growth Oil
19. [All Beauty] Hair Feel Finishing Stick, Hair Finishing Stick, Hair Feel Stick, Small Broken Hair Finishing Cream, Hair Styling Wax Stick Hair Gel for Woman, Men- Moisturizing ＆ Shiny
20. [All Beauty] Herbal Essences Hair Conditioners moisture rosemary & herbs 6 oz,pack of 1
21. [All Beauty] Hot Tot Shampoo Extra Gentle, Tear-Free, Mild for Daily Use, with Green Tea and Aloe Vera, Cruelty-Free, Soy-Free, Hair Care For Babies Toddlers and Children 8 ounces
22. [All Beauty] Ichi Hair Waso Oil 50mL
23. [All Beauty] Jane Angels Kit Fruit Fusion Melon – Shampoo and Hair Conditioner, Hydration and Strengthening, Professional Salon Quality Brazilian Hair Care, Rich with Ingredients from Brazil’s Rain Forests
24. [All Beauty] Koncept Pro Thickening Biotin Conditioner 960ml
25. [All Beauty] London Grooming Hair Styling Cream (100ml / 3.4oz)
26. [All Beauty] Magic Hair Therapy Tratamiento Capilar Restaurador Diurno con frutas naturales contiene aguacate. Capilar Treatment for the night.
27. [All Beauty] Micrinpe 3-Second Hair Straightening Cream with Comb,Hair Straightening Treatment Cream for Dry and Curly Hair, Nourishing Fast Effective Just In 3 Seconds (2Pcs)
28. [All Beauty] Microfiber Super Absorbent Hair Towel, Dry Hair Cap (4 Pack)
29. [All Beauty] Nair Hair Remover Nourish Skin Renewal Face 3 Ounce (88ml) (6 Pack)
30. [All Beauty] Naturelle Hypo-Allergenic Styling Gel
31. [All Beauty] Nick Chavez Velvet Mesquite Serum For Hair & Skin 4 oz Double Size
32. [All Beauty] On Organic Natural Curl-N-Wavy Avocado Detangler 8 Oz (Pack of 2)
33. [All Beauty] Pantene Pro-V Ultimate 10 Bb Shampoo, 21.1 Fluid Ounce
34. [All Beauty] Parachute Advansed Men Hair Cream,Classic 100 gm (Pack of 3)
35. [All Beauty] Privé Blonde Rush Shampoo ( 32 Fluid Ounce / 946 Milliliter ) - Unparalleled Shine to Your Blonde Hair to Keep Your Blonde Catwalk Cool and Fabulous
36. [All Beauty] Quantum Insite (for Delicate Hair)
37. [All Beauty] SCALP D Beaute Shampoo (11.83Fl Oz) (Japan Import)
38. [All Beauty] Salerm HI REPAIR Shampoo & Mask Conditioner DUO SET, High Repair Damaged Hair for Strong, Full Bodied Shine Softness (W/Sleek Comb) Masque (1000 ml (36 oz) + 1000 ml (36 oz) LARGE DUO KIT)
39. [All Beauty] Salerm Vison Permanent Hair Color and Developer (1 Color and 1 Developer Set) (20 vol 8.1 oz, 3)
40. [All Beauty] Salon Labs Chemistry Hydrate Ultra Moisture Leave-In Conditioner 6 fl oz (177 ml)
41. [All Beauty] Shower Caps Disposeable (100 pcs + 30 pcs) Plastic Hair Cap, Large Thick Waterproof Clear Bath Shampoo Caps for Women, Girls, Hotel, Spa, Travel and Home
42. [All Beauty] Spapharma Leave In Curly Hair Conditioner With Tea Tree Oil, Argan & Jojoba Oil, Shea Butter, Dead Sea Minerals, Rose Of Jericho and Keratin for Softness and Tight Curls
43. [All Beauty] Sparks Long Lasting Bright Hair Color - Mermaid Blue 3 oz. (Pack of 2)
44. [All Beauty] Star Bio Complex Coconut High Shine Deep Hair Conditioner, Set for Damaged Hair, For Dry and Fragile Hair, Self Hair Care, Miracle Treatment for All Hair Types, 4 Count
45. [All Beauty] Swiss-o-Par Argan Oil Shampoo 250 ml / 8.3 fl oz
46. [All Beauty] Top Secret Hair Thickening Fibers - Compact Design - Light Brwn (.25 OZ.)
47. [All Beauty] Vitress Hair Polish
48. [All Beauty] Volumizing Spray - Thickening Texture Spray Gives Full, Voluminous Hair - Strengthen, Combat Oil, and Prevent Hair Loss - Panthenol, Burdock Root, Fenugreek for Hair Growth, Shine, Volume by Osensia
49. [All Beauty] Wildroot Hair Groom Conditioner 3.38oz (100 ml.)
50. [All Beauty] Wonder Gro Shea Butter Hairdress 6 oz.

Return JSON only with this schema:
{
  "cluster_id": 5,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 6

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 6
Cluster size: 754

Representative product titles:
1. [All Beauty] 10 Pieces Gel Nail art Brushes Dotting Pens Acrylic Nail Brush Painting Drawing Detailing brushes Double Ended Tools Include Art Sculpture Pen for Nail Design
2. [All Beauty] 10 Pieces Nail Art Pens Kit Include Liner Brushes and Gel Painting Dotting Acrylic Nail Brush Pens (Style Set 2)
3. [All Beauty] 100% Kolinsky Acrylic Nail Brush #8, Handle Brush for Nails, Wood Nail Art Brush, Acrylic Application Polygel Brush, Manicure Tool, 1 Piece
4. [All Beauty] 2 Pcs Flatback Rhinestones About 4510 Pcs Colorful Nail Art Rhinestones Flatback Crystal Colorful + Deep Blue Rhinestone with Wax Pen Tweezer for Nails Art Crafts and Face Eyes Makeup
5. [All Beauty] 500PCS Clear False Nails Tips, Half Cover Lady French Style Acrylic Artificial Tip
6. [All Beauty] 500pcs Coffin Ballerina Nail Tips Fashion Long False Nails Tips Half Cover DIY Acrylic Fake Nails 10 Sizes (BEIGE)
7. [All Beauty] 8 Pieces 3D Nail Art Brushes Set Nail Art Liner Ombre Brush Nail Painting Brushes Double Ended Nail Dotting Drawing Pen Acrylic Rhinestone Handles Nail Art Pens
8. [All Beauty] AIQIUSHA Nail Polish Remover, Quickly Bursting Removes Soak-Off Gel Nail Polish 15ML/PC (2pcs)
9. [All Beauty] Acrylic French Nail Tips,1000 pcs False Nails with Glue - Clear or Natural for choose, Fakes Nails Full Cover,for Nail Salons and DIY Nail Art(10 Sizes)
10. [All Beauty] Adoree Nail Lacquer Cordon Blue .5oz
11. [All Beauty] AiQueen 2 Sets Nail Clippers Stainless Steel Manicure Pedicure Set Personal Care Nail Utility Grooming Kit with Portable Case (7 Pcs Per Set)
12. [All Beauty] AwsmColor No Wipe Gel Top Coat, 10ml Soak Off UV LED Gel Top Coat for Gel Nail Polish Mirror Shine Finish Long Lasting
13. [All Beauty] BORN PRETTY Nail Polish Polish Pearl Transparent Shell Glimmer Shiny Shimmers Manicuring Art Varnish 5 Colors with 2 in 1 Top Base Coat
14. [All Beauty] Best Crystal Glass Nail File – Perfect for Women & Girls - Long Lasting Double Sided Tempered Glass – Professional Salon Manicure/Pedicure Filing Tool for Natural Nails - with Case - Light Pink
15. [All Beauty] Bling Art Almond False Nails Fake Stiletto Gel Silver Glitter 24 Long Tips Glue
16. [All Beauty] China Glaze Nail Polish, #Thisismystreet 1693
17. [All Beauty] Electric Nail Drill Adjustable Speed Professional Nail Drill Kit For Acrylic Gel Nails Manicure Pedicure Polishing Tools with 11Pcs Nail Drill Bits and 16 Sanding Bands
18. [All Beauty] Gel Glam 24 Nails,Frosted Short Fashion False Nails (Geometric patterns AL299#)
19. [All Beauty] JYS Glitter UV Gel Nail Polish,Nail Art Gel Polish,Starry Glitter Gel,Chameleon Gel,Diamonds Gel Nail Polish Nail Art Gel Polish UV LED Gel Polish
20. [All Beauty] Jolie Vegan 2 Piece Nail Polish Set - Vegan, Cruelty-Free Nail Polish, Promotes Mental Health, Non-Toxic Formula, 11-Free, PETA Certified, 0.5 Fl. Oz. each (You Are Amazing & Positive Thoughts)
21. [All Beauty] JoyKott MATTE Nail Powder Chrome Metallic Manicure Pigment NEW on Amazon (Matte Gold)
22. [All Beauty] Kiss imPress Press-On Manicure Periwinkle Blue Nails Flash Mob
23. [All Beauty] Kleancolor 6 Nail Polish Metallic Color Rose Lilac Silver Teal Penny Sand Lacquer Manicure KC-NEWMT01 + Free ZipBag
24. [All Beauty] Konad Professional Set B for Stamping Nail Art
25. [All Beauty] Konad Set Starter Kit for Stamping Nail Art (C-B SET)
26. [All Beauty] Lacross Nail Clip - Christmas Design on packaging
27. [All Beauty] Lagunamoon Gel Nail Polish, Soak Off UV LED Nail Manicure Color Gel Polish Varnish Set 6PCS 8ML - Love Spectrum
28. [All Beauty] Lavinda Gel Nail Polish Set , 6 Macaron Colors Pink Yellow Green Blue Nude Purple Festival Holiday Gel Polish Kit with Gift Box, Soak Off UV LED Lamp Required for Home Use Gel Polish Set
29. [All Beauty] Maniology (formerly bmc) Cute Colorful Mixed Pattern 6pc 1mm Thin Nail Stamping Scraper Card Set - Tropicana Charms
30. [All Beauty] Mobray Color Changing Gel Nail Polish Temperature Change Color 6 Colors Mood Soak Off UV LED Glitter Gel Nail Polish Set 12ml Nail Art Gift Box (Set 3)
31. [All Beauty] Nizi Jewelry Nail Art Marbleizing Painting Nails DIY Tools Dotting Pen 1pcs Rhinestones Box Plastic Plate 1pcs Gel Cube 1pcs 3pcs/Set
32. [All Beauty] Orly Nail Lacquer - ELECTRIC ESCAPE Summer 2021 Collection - Pick Any Color .6oz/18ml (OR2000099 - Synthetic Symphony)
33. [All Beauty] Orly Nail Polish Color Lacquer Set 6-Piece Collection #72
34. [All Beauty] Outyua Glossy Press on Nails Pink Gradient Medium Fake Nails Acrylic Full Cover Square False Nails Prom for Women and Girls 24pcs
35. [All Beauty] Pink Gellac 125 Bronzy Pink Soak-Off UV/LED Gel Polish
36. [All Beauty] Portable Electric Nail Drill Nail kit for beginners with 11Pcs Nail Drill Bits Polishing Shape Tools Acrylic nail set design for Home Salon Use
37. [All Beauty] Premium Salon Acrylic French Nails Natural French Long/Medium False Nails 24PCS/PACK
38. [All Beauty] Press on Nails Coffin Medium Length False Nails for Women, 96 PCS TNWZC Stick on Nails for Girl Ballerina Professional Artificial Nails, Acrylic Press on Nails
39. [All Beauty] Professional Red Wood Kolinsky Acrylic Nail Brush Round Size 8
40. [All Beauty] Revel Nail Dip Powder Starter Kit (4 pcs)
41. [All Beauty] Revel Nail Dip Powder | for Manicures | Nail Polish Alternative | Non-Toxic & Odor-Free | Crack & Chip Resistant | Can Last Up to 8 Weeks | 1oz Jar | Mood Changing | Lynx
42. [All Beauty] TOMICCA Gel Nail Polish Set, Pink Red Green, 6 Spring Summer Color Gel, Soak Off Gel Polish Starter Kit, UV LED Gel Manicure for Home & Salon, No Chip, Non Toxic - 6 × 8ml
43. [All Beauty] Tubran 6 Color/Kit Glitter UV Gel Nail Polish Set Color UV LED Nail Gel Varnish Semi Permanent Nail Lacquer Soak Off Sequins Gel(Solid Color Series)
44. [All Beauty] Vcedas French Nail Tips 1.18 Inch Half Cover False Nails 200PCS Lady French Acrylic Style Artificial False Nails (Clear)
45. [All Beauty] WOKOTO 100 Pcs Fiberglass Nail Art Form Fiber Quick Building False Nail Extension Nail Acrylic Tips Manicure Accessories
46. [All Beauty] WOKOTO 6Pcs Nail Wraps For Women Sticker Nails With 1Pc Nail File Kit Full Nail Tips Stickers Wraps For Nails
47. [All Beauty] Wishesport Nail Care System -Electric Manicure/Pedicure Tool. Easily File, Buff and Shine Fingernails Nail Tools Set Nail Polisher
48. [All Beauty] Woeoe Glossy Press on Toenails Silver Short Acrylic Fake Toenails Full Cover Bling Rhinestones Clips False Toenails for Women and Girls (24Pcs)
49. [All Beauty] essence The Gel Nail Polish, 21 A Whisper of Spring
50. [All Beauty] iyesku Portable Electric Nail Drill Machine, Professional USB Pedicure Drills for Acrylic Nails Gel Polishing Shape Tools with Nail Drill Bits and Sanding Bands, 2020 Upgraded Nail Drill Kit -Pink

Return JSON only with this schema:
{
  "cluster_id": 6,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 7

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 7
Cluster size: 523

Representative product titles:
1. [All Beauty] 10 Pack Velvet Scrunchy Elastics Rabbit Ears Scrunchies Bobbles Soft Elegant Elastic Hair Bands Hair Tie
2. [All Beauty] 15Pcs Clear Spiral Hair Ties No Crease Elastic Ponytail Holders Phone Cord Traceless Hair Ties for Women Thick Hair by Accmor On Sale
3. [All Beauty] 20 Pcs Multicolor Snap Pearl Hair Clip Fashion Geometric Pearl Shape Hair Clips Plastic 10 Bright Color Hair Barrettes for Women Ladies Party Wedding Daily
4. [All Beauty] 3Pcs Deft Bun for Hair, Hair Bun Maker for Women Magic Donut Hair Bun Maker Hairstyle Bun Shapers Reusable French Twist Hair Clip For Girls
5. [All Beauty] 6PCS Bun Hair Nets Set Reusable Elastic Mesh Bun Cover for Ballerina Dancer Bank Clerk Nurse Skater Hair Fixing Black Stretch Lace Hair Accessories for Women Girls Mixed Style-3 (Type-1)
6. [All Beauty] 8 Pieces Large Metal Claw Clips Hollow Non-slip Hair Catch Jaw Clamp for Women Girls Hair Barrette for Fixing Hair(Gold, Silver, Rose Gold, Black, 8 Pieces)
7. [All Beauty] AISI BEAUTY 8'' Bob Style Human Hair Crown Topper with Bangs Clip in Top Hairpieces Closure for Women with Thinning Hair Gray Hair/Hair Loss (Base 3''X4'', Dark Brown)
8. [All Beauty] Accesyes Plumeria Hair Clips Hawaii Hairpin Bobby Pin Flower Foam Hair Clip Plumeria Rubra Flower Headpiece Accessory Hair Combs (White)
9. [All Beauty] AeraVida Cute and Colorful Light Pink Tropical Flower Leather Hair Clip
10. [All Beauty] Afro Puff Drawstring Ponytail for Black Women Short Curly Synthetic Hair Bun Extension, Updo Ponytail Hair Piece with Two Clips (2#)
11. [All Beauty] Baby Gril Hair Clips and Bow Barrettes Girls Hair Accessories for Baby Girl Toddlers Teens Kids Womens (Mixed 20 Colors)
12. [All Beauty] Baby Wisp Mini Latch Clip Grosgrain Cadeau Bow Baby Girls Fine Hair (Red)
13. [All Beauty] Bachelorette Party Hair Ties with Laser Diamond Card,Bridesmaid Proposal Gifts Set of 7,Spiral Hair Ties Scrunchies,Bridal Shower Wedding Favors Souvenirs Decorations for Guest (Purple)
14. [All Beauty] Baisidai Brown 1000-Pack of Silicone Micro Rings Links Beads For Human Feather Hair Extension Tip
15. [All Beauty] Big Hair Clips 4.35 Inch Nonslip Large Claw Hair Clips Strong Hold Large Hair Clips for Thick Hair Matte Styling Hair Clips Perfect for Women Long Heavy Hair
16. [All Beauty] Bows for Belles Alligator Hair Bow Ribbon Sculpture (Orange) Made in the USA
17. [All Beauty] Braided Hair Clips for Women Girls, Sparkling Crystal Stone Braided Hair Clips Barrette with 3 Small Clips, Triple Hair Clips with Rhinestones for Sectioning,8PCS (8pcs-Mix)
18. [All Beauty] Clione 3 Packs Jamaican Bounce Crochet Hair Wand Curly Braids Synthetic Twist Hair （T30）
19. [All Beauty] Elcoho 24 Pieces Rhinestone Bobby Pin Metal Crystal Hair Clips Hair Barrette Clip Decorations for Women or Girls (Silver, Black)
20. [All Beauty] FRCOLOR Ponytail Hooks Headband Hair Claw Hair Clips Rubber Bands Hair Styling Hair Braid (18pcs)
21. [All Beauty] Fani 150 Pcs Clips 9-Teeth Snap-Comb Wig Clips with Rubber for Hair Extension Wigs Weft Hairpiece DIY Clips (Black)
22. [All Beauty] HANYUDIE Messy Bun Hair Piece Synthetic Messy Bun Scrunchies Extensions Hairpiece Curly Wavy Messy hair pieces for women (Medium Warm Brown)
23. [All Beauty] HAYLEY Clip On Hairpiece by Mona Lisa - 130 Copper Red
24. [All Beauty] Hair Claw Clips 12 Colors, Vintage Simple Irregular Non Slip Hair Accessories Claw Clips for Women Girls, 12 PCS
25. [All Beauty] Halloween Girls Womens Korker Hair Bow Hair Clip Grosgrain Ribbon Bow with Alligator Clip Teens Set of 2 (Boo & Polka Dot)
26. [All Beauty] Hepburn Hair Bun 80g #1 Dark Black
27. [All Beauty] Jaciya 3 Pack Retro Flower Butterfly Style Hair Clips Hair Barrette Hair Pin Barrettes Spring Clip for Women, 3 Colors
28. [All Beauty] LOKNGXU Hair Claws for Women Large Claw Clips for Thick Hair Strong Hair Claw Clips Girls for Thin Hair Matte Claw Clips Multiple Style Options (style 7)
29. [All Beauty] Magic Hair Bun Maker,5pcs Pearl Flower Donuts Maker Twist Headband Bud Headwear DIY Hairstyle Tool For Ballet, Wedding, Yoga, Dancing, Party
30. [All Beauty] Magic Hair Clips, Hairclips for Women, Girl, Ladies, Magic Hair Comb, Double Comb Hair Clip, Stretch Hair Comb for Women, Girl, Ladies-5 PCS
31. [All Beauty] Magigift 20 Pack Solid Color Hair Scrunchies Ponytail Holder Elastic Cotton Stretch Hair Ties - Cotton Fabric Hair Accessories For Women or Girls
32. [All Beauty] Maysky Spiral Spin Screw Pin Hair Clip Twist Barette Hairpin Bridal Hair Pins,Twist Screw Hair Pins,10 Pack
33. [All Beauty] Milky Way Organique Pony Pro Express Wrap Ponytail Mali Curl (1B)
34. [All Beauty] Pangda 7 Pieces Hair Comb 20 Teeth Rhinestone Comb Pin Clip Bridal Hair Combs Accessory for Women Girls, Assorted Colors
35. [All Beauty] Parcelona French Crab Interlocking Savana Light Shell Large 3.5” Celluloid Hair Clip Side Comb for Women and Girls
36. [All Beauty] Potato001 Shiny Rhinestone Hair Ties Bands Rings Ponytail Holders Girls Women Gift - AB + White S …
37. [All Beauty] RACILY Human Hair Ponytail Wrap Drawstring Natrual Black (12", Kinky Straight)
38. [All Beauty] Ribbon Hair Ties No Tangle No Crease Tie Dye Multi Color 30 Pack
39. [All Beauty] SHUOHAN 1 Pcs Tousled Curly Messy Hair Bun Updo Hair Piece Ponytail Silver Hair Extension Synthetic Hair Extensions Scrunchies Hairpiece for Women (1001A#)
40. [All Beauty] Samtiny 14Pcs Rainbow Hair Clip Fashion Pearl Hair Clip Sweet Artificial Macaron Resin Hair Clip Suitable for Women Hair Clips Hair Accessories Styling Tools 1 Yellow 14 piece set
41. [All Beauty] Sparkling Crystal Stone Braided Hair Clips, 4PCS Rhinestone Hair Clips for Hair Sectioning, Satin Fabric Hair Bands, Satin Fabric Hair Bands, Hair Jewelry for Braids, Multi Clip Hair Barrette
42. [All Beauty] TANG SONG 3PCS Crystal Vintage Metal Hair Claw Clips Hair Catch Barrette Jaw Clamp for Women Half Bun Hairpins for Thin Hair
43. [All Beauty] TOBATOBA 18pcs Hair Scrunchies Flowers Elastic Hair Bands Scrunchy Hair Ties Ropes Scrunchie Hair Scrunchies Bunny Ears Hair Bow Chiffon Ponytail Holder for Women
44. [All Beauty] Tara Girls Twinbead Multi Cute Design Ponytail Elastics Pack Of 2 (BTW6)
45. [All Beauty] URBEST Hair Coils, Tie Hair, Spiral Hair Ties,Phone Cord Hair Ties, Elastics Hair Tie, No Crease Hair Ties, Coil Ponytail Holder (Blue)
46. [All Beauty] Wedding Decor Vintage Red Flower Hair Stick Jade Beads Decor Tassel Hairpin for Ladies Vintage Decor
47. [All Beauty] YAIKOAI 6 Pieces Large Grip Octopus Clip Matte Hair Claw Clips Spider Hair Jaw Clamp Barrettes for Women Girl Thick Long Hair Headwear, 6 Colors
48. [All Beauty] YMHPRIDE 2 PCS Hair Bangs Clip in Human Hair Dark Red Brown Clip in Hair Bangs Fringe Hairpieces Flat Air Bangs Straight Flat Bangs with Temples for Women
49. [All Beauty] Yeshan Women Rhinestone Crystal beaded Flower Pattern Hair Barrettes Clips,Golden
50. [All Beauty] uxcell Lady Rhinestone Decor Light Purple Bowknot Shape Barrette Hair Clip w Snood Net

Return JSON only with this schema:
{
  "cluster_id": 7,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 8

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 8
Cluster size: 550

Representative product titles:
1. [All Beauty] 10 Pack Wide Headbands, 4 Style knot Turban Hairband Vintage Head wrap Hair Band Elastic Hair Accessories
2. [All Beauty] 10 Pcs Headbands for Women,bebeepoo Knotted Headbands Top Knot Hair Bands for Women's Hair Thick Turban Headbands Leopard Print Cheetah Headband Fashion Headband for Women and Girls
3. [All Beauty] 12pcs Baby Girls Turban Knotted Headband Elastic Bows Hair Band for Infants Toddler Newborn
4. [All Beauty] 3 Pieces Soft Sleep Cap – Night Satin Bonnet with Wide Premium Elastic Band for Women
5. [All Beauty] 3 Pieces Twist Head Wrap Headband Headscarf Twist Bow Wired Headbands Scarf Wrap Hair Accessory
6. [All Beauty] 4 pcs: HBY Women's Fashion Winter Button Ear Warmer Crochet Headband Hairband Wrap
7. [All Beauty] 48 Pieces Softball Accessories Set Includes 24 Pieces Softball Bracelets Softball Wristband Silicone Bracelet 24 Pieces Softball Hair Ties Sports Elastic Headband for Girls Softball Player Party Favor
8. [All Beauty] 6 Pieces Shower Cap for Women Reusable Hair Shower Cap Waterproof Bowknot Bath Caps Adjustable Bow Bath Caps for Girls Long Hair Shower Bathing Spa Home Travel, 6 Styles
9. [All Beauty] ASHILISIA Super Soft Men Durag Headwraps (2 PCS) with Extra Long Tail and Wide Straps for 360 Waves, Light Green&black+red&black, Free size
10. [All Beauty] Amoretu 4 Pack Women Boho Headband Elastic Fashion Tropical Turban Twisted Hair Headbands
11. [All Beauty] Baby Girl Bows Headbands Hair Accessories for Newborn Infant Toddler Girls' Shower (Boheme-7Pcs)
12. [All Beauty] Barara King 4 Pack Bow Women Headband Boho Floal Style Criss Cross Head Wrap Hair Band
13. [All Beauty] Black Metal Headbands for Women, Hair Accessories (6 In, 10 Pack)
14. [All Beauty] Bohend Boho Headbands Wide Flower Hair Band 6PCS Boho Bandeau Stretchy Athletic Daily Use Hair Accessories for Women and Girls (B)
15. [All Beauty] Bohend Fashion Headband Wide Pure Knotted Daily Use Travel Outdoor Hair Band Elastic Yoga Sport Hair Accessories for Women and Girls(6pcs)
16. [All Beauty] Chew-Bacca Peter May-Hew Rave Face Bandana For Men Women Neck Gaiter Scarf Dust Wind Uv Protection Outdoor Hiking Cycling Balaclava Headwear
17. [All Beauty] Duoqu 12 Pcs 4.1" Baby Girls Soft Headbans With Big Hair Bows Flowers
18. [All Beauty] ELABEST Yoga Headband Wide Headbands with Button 3Pack Sport Hair Band White Head Wrap Ear Protection Bandeau Elastic Head Band for Women and Girls
19. [All Beauty] Elegant Princess Style Wide Lace Rhinestone Hair Band Hair Hoop Headband Hariband Headwear Hair Accessories for Women Lady Girls
20. [All Beauty] FAELBATY 2 Pcs Headbands for Women Knotted Headbands Glitter PU Wide Headbands for Women Cute Hairbands Fashion Knot Headband for Women(Black & Silver)
21. [All Beauty] Foamee 2 Packs Working Caps Women with Buttons & Sweatband, Hair Covers Bouffant Working Hats Women Long Hair Ponytail Cap, Chef Hats Ribbon Tie Back Caps for Women & Men, Adjustable Shower Caps H
22. [All Beauty] Goody Styling Essentials Shower Cap, 3 Count (4-Pack)
23. [All Beauty] HORSE Headband Personalized With EMBROIDERED Custom Name By Funny Girl Designs (LAVENDER HEADBAND)
24. [All Beauty] Hair Cutting Cape for Adults - Polka Dots Print - 100% Polyester Lightweight Water Resistant Hair Cape - 57in x 50in - Snap Closure - Haircut Cape - Salon Cape
25. [All Beauty] Headbands For Women Cotton Stretch Headbands Elastic Yoga Hairband for Teens Girls Women Adults, Assorted Colors, 10 Pieces (Black)
26. [All Beauty] Headbands for Women 20 pcs, Boho Floal Style Criss Cross Head Wrap Hair Bands with 1 Storage bag
27. [All Beauty] MHDGG 1Pcs Knotted Headbands for Women Sequins Bandana Headband Turban Headbands Wide Headbands for Girl Hair Bow Hair Band for Women Headwear,Caramel
28. [All Beauty] MHDGG Bandana Headband for Women,Rhinestone Knot Headband Shining Pearl Headband Handmade Turban Hair Hoops Accessories Hair Hoops with Bow Cross Head Band Wrap,Pink
29. [All Beauty] MHDGG Headbands for Women Knotted Headbands Rhinestone Diamond Turban Headbands for Women Wide Headbands for Women Vintage Hairband Hair Hoops Hair Accessories,Leopard Yellow
30. [All Beauty] Meartchy Knotted Headbands for Women - Solid Color Hair Hoops - Cross Knot Hairbands with Cloth Wrapped for women and Girls - 5Pcs
31. [All Beauty] Nydotd 4pcs Wide Band Satin Bonnet Night Sleep Cap Sleeping Head Cover Comfortable Night Sleep Hat Soft Silky Hair Loss Cap for Women Girls (Medium)
32. [All Beauty] PUSSAER 4Pack Printed Shower Cap for Women Long Hair, Reusable EVA Extra Large Shower Hair Hat, Double Waterproof Protection, Kids, Men(Modern Fresh Natural Pattern 13 inches)
33. [All Beauty] Padded Headband Satin Fashion Headbands for Women multi-color Statement Light thick sponge plastic Retro Grace Elegant Wide Plastic Hairbands For Woman
34. [All Beauty] Parcelona French Broad Tortoise Shell Brown 2 Inch Very Wide Flexible Celluloid Acetate Headband for Girls and Women
35. [All Beauty] Pearl Headband for Women Girls Fashion Hair Accessaries Wide S.Cafe Mesh Fabric Cross Knot Pearl Hair Hoop for Wedding Party
36. [All Beauty] Playbuy LED Flower Garland Wreath Headband(2pcs) -Wedding wreath Crown Festival Floral for Party Festival Wedding
37. [All Beauty] QUEYING Braid Headband For Women Looking Natural Fashion Beauty Synthetic Elastic Fishtail Hair Band Accessories Extension - Golden Red (27A-30B-30A)
38. [All Beauty] QadiraQian 3 Pcs Pearl Headband Colourful Beaded Headband Wedding Party Headbands Sets Bridal Fashion Hair Accessories for Women Girls Kids
39. [All Beauty] Qandsweet Baby Girl's Headbands and Bows Hair Accessories (10pcs Newest03)
40. [All Beauty] Scala Women Lady Girls Fashion Cute Simple Headband Hair Head Band Party Gift Cosplay Rose Cat Ears Headwear Flower Hairband Accessories (Pink)
41. [All Beauty] Shemay Fashion Solid Grosgrain Ribbon Hair Bows and Headbands for Toddlers Girls Kids
42. [All Beauty] Silver Embossed Squares Headband Solid Hair band for Women and Girls
43. [All Beauty] Skinny Cloth Headbands Fashion Fresh Color Flower Spring Flora Hairbands Non-Slip Sweet Hair Hoop for Girls Hair Accessories Pack of 5
44. [All Beauty] Taomoder 12 Packs Boho Headbands for Women Turban Headbands for Women Fashion Hairbands Hippie Headband Bohemian Floral Style Workout Headbands for Women Boho Hair Accessories
45. [All Beauty] Women Headbands, Elastic Headbands with Buttons, Headbands with Buttons for Women Men, Non Slip Hair Bands for Yoga Sports Running (HHNK04)
46. [All Beauty] Women's Vintage 1920s Great Gatsby Flapper Headband Feather Wedding Party Headpiece (#3 Black)
47. [All Beauty] Yeshan Rhinestone and Crystal Beaded Flower Design Plastic Headband, Hairband for girls,Pink and ab white
48. [All Beauty] Yeshan Rhinestone and Crystal Beaded Flower Design Plastic Headband, Hairband for girls,White
49. [All Beauty] Zucker Feather (TM) - Marabou Antenna Headband w/Lurex Dark Lilac/Opal Lurex
50. [All Beauty] sold out Shower Caps, Shower Caps for Women, Waterproof Bath Caps Plastic Reusable

Return JSON only with this schema:
{
  "cluster_id": 8,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 9

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 9
Cluster size: 380

Representative product titles:
1. [All Beauty] 100 Rings Glue Cup Holder and 100 Eyelash Brushes Applicators for Eye Lash Extension Mascara Wands Disposable
2. [All Beauty] 100% Pure Cotton Amblyopia Cute Cartoon Eye Patch for Glasses Lazy Eye Amblyopia Strabismus Treat Eye Patches for Children Kids (Left Eye)
3. [All Beauty] 25mm Lashes Mink 1 Pair False Eyelashes Dramatic Look Lashes 25mm HICOCU…
4. [All Beauty] 3D Mink Lashes 25mm Lashes Handmade Volume Thick Mink Eyelashes 3 Pairs Ruairie
5. [All Beauty] 4D Silk Fiber Lash Mascara & Fiber 2-in-1 Double-End Black Brown Blue Mascara Volume Set(3-Pack), for Thickening and Lengthening, Waterproof Smudge-Proof HypoallergenicThicker and Longer Lashes DNM
6. [All Beauty] 4D Silk Fiber Lash Mascara, Black Color & Glitter Macara - Voluminous Extension for Longer Sparkling Diamond Shining Eyelashes, Natural Non-Toxic Hypoallergenic Eye Makeup Set (#1 Black)
7. [All Beauty] 5 Style Mix 10 Pairs False Eyelashes Natural Look 3D Fake Lashes Small Face Eyelashes 100% Handmade Lashes Wispies Short Soft Reusable Eye Lash Transparent Band Eyelash 1 Pack by EMEDA
8. [All Beauty] 6 Pieces Double Layer Eyelash Packaging Circle Box Eyelash Storage Box Case Lash Boxes Empty Lash Case with Mirror and Tray for Women Girls, Rose Red
9. [All Beauty] ALICROWN False Eyelashes, Natural Soft Handmade Lashes 5 Pairs Multipack with Glue and Applicator
10. [All Beauty] ALICROWN Lashes Faux Mink Fluffy Lashes 3D Volume Natural Fluffy Lashes Pack False Eyelashes Natural Look
11. [All Beauty] BEPHOLAN Mink Eyelashes, 3D Lashes Mink,Siberian Mink Fur False Eyelashes,Dramatic Round Look,100% Handmade & Cruelty-Free Fluffy Volume wispy lashes,1 Pair XMZ004
12. [All Beauty] BEYELIAN Premade 6D Volume Fans Lashes Semi Permanent Eyelash Extensions Individual Cluster False Eyelashes (0.05mm 11mm C Curl 108 pcs)
13. [All Beauty] Blue Eyes Lashes Mascara Applicator / Application Guiding Tool With Eyelashes Comb And Pink Silicone Blackheads Facial Pores Cleaner / Face Skin Cleanser By VAGA
14. [All Beauty] Cat Eye Lashes Pack False Eyelashes Full Fluffy Medium Volume 3D Faux Mink Lashes Wispy 4 Styles 17-19mm Soft Reusable Handmade Fake Eyelashes, 16 Pairs Pack by Pawotence
15. [All Beauty] EMEDA 8D Volume Lash Extensions .07mm C Curl 8-15mm Mixed Tray Premade Volume Eyelash Extensions Small Thinner Base Russian Volume Pre Made Lash Fans (0.07 C 8-15 Mix)
16. [All Beauty] Ellipse Eyelash Extensions 0.15-D Curl 11mm Flat Light Lashes Matte Individual Eyelashes Salon Use 0.15/0.20mm C/CC/D/DD Curl Single 8-16mm Mix 8-15mm（0.15 D 11mm)
17. [All Beauty] Eyelash Extension Supplies 0.05 D Curl 13mm Individual Lash Extensions Silk Professional Salon New Material|0.03/0.05/0.07/0.10/0.15/0.20 C/D Curl 10-16mm Mix 8-15mm|(0.05 D 13mm)
18. [All Beauty] Eyelash Growth Serum 5Ml 100% Natural Material- Grow Longer Fuller Eyelashes VIOCOODA Enhancing Serum & Eye Lash And Eyebrow Growth Serum Safe For Extensions.Dermatologist Certified & Hypoallergenic
19. [All Beauty] FANICEA 4D Silk Fiber Lash Mascara with 2 Pcs Eyeliner Gift Set Natural Voluminous Waterproof Long Lasting No Smudging Lengthening Thickening Eyelash Cosmetics Kit for Women Girls
20. [All Beauty] Faith Beauty Longer Dual Magnet False Eyelash (Dual Magnet,)
21. [All Beauty] False Eyelashes,Laimeng A Pair Natural Beauty Dense False Eyelashes
22. [All Beauty] Flat Lashes C Curl 0.20mm 8-14mm Mixed Tray Ellipse Eyelash Extensions Volume Lashes Individual 3D Salon Perfect Use by FADLASH
23. [All Beauty] Fluffy Manga Lashes Natural Mink False Eyelashes Wispy Anime Japanese Asian Eye Lashes Pack 14 Pairs 5D Volume Fake Eyelashes
24. [All Beauty] Homtone 3 Layers Acrylic False Eyelash Organizer Case Display Box for 18 Pairs Eyelashes Transparent Storage Box, Size 6.7x4.7x2.5inch
25. [All Beauty] JIMIRE Full False Eyelashes Natural Volume 3D Lashes Pack 10 Pairs
26. [All Beauty] Jordana Best Length Extreme Lengthening Mascara (Black, 3 Pack)
27. [All Beauty] KYRA COSMETICS LASH Magnetic Eyelashes kit with Eyeliner, Travel size EyeLash Case and Tweezer - Natural Looking Reusable lashes Waterproof Eyeliner 10 pairs of 6D False Long Short
28. [All Beauty] LASHVIEW DIY Eyelash Extension Remover
29. [All Beauty] LVMIX 20mm Mink Lashes Pack 3D Dramatic False Eyelashes Fake Lashes Cruelty-free and Reusable 3 Styles
30. [All Beauty] MAKEUP ZONE False Eyelashes Natural Look Reusable Short Volume Fluffy Eyelashes Wispy Lashes 10 Pairs(Lashes-16)
31. [All Beauty] MISMXC Magnetic Eyeliner and Eyelashes Kit,Upgraded 3D Magnetic Eyelashes and Eyeliner Set with 10 Pairs Reusable Magnetic Lashes &2 Tubes of Magnetic Eyeliner&1 Tweezers-No Glue Need
32. [All Beauty] Magnetic Eyelashes Kits Set, 2019 Minso Natural-looking Design Magnetic Eyelashes with Magnetic Liquid Eyeliner and Delicate -box ，Easy-wearing & Reusable Eyelashes
33. [All Beauty] Magnetic Eyelashes with Eyeliner 5 Pairs Reusable Fake Eyelashes No Glue 2 Only Magnetic Eyeliner 3D eyelash sets (Girl Pink)
34. [All Beauty] Mannequin Head with Removable Eyelids Eyelashes Extension Supplies with 4 Pairs Replaced Eyelids Makeup Rubber Silicone Training Mannequin Head Lash for Practice Eyelash Extensions (light pink)
35. [All Beauty] Mirenesse Magnomatic 24hr Magnetic Eyeliner & Reusable 5D False Lashes,Safe. Easy No Adhesive No Mess, Vegan & Toxin Free, 2 Pairs Volume Vivian Day & Night + Magnetic Liner 0.17oz
36. [All Beauty] Newcally Lashes Fake Eyelashes Long Dramatic Fluffy Wispy Crossed Faux Mink Eyelashes Thick Volume Lashes Pack
37. [All Beauty] PDO Threads(Eye thread 30G 25mm) Face Lift/Whole Body Lifting Mono Blunt Threaad Eye Lift(20pieces per pack)
38. [All Beauty] Pawotence False Eyelashes 25mm Dramatic Long Faux Mink Lashes Pack 10 Pairs Soft Handmade Fake Eyelashes Pack
39. [All Beauty] Premade Fans Eyelash Extensions 12D-C-12 280 Fans Premade Volume Eyelash Extensions Pointed Base Fans 0.07 Premade Volume Fans C D Curl (12D-C,12mm)
40. [All Beauty] Professional Lash Eyelash Perm Lotion #1 Pink Bottle & #2 Blue Bottle (2 Bottles in a Set)
41. [All Beauty] QUEWEL Volume Eyelash Extensions | 0.03-0.12mm | C/CC/D/DD Curl | 8-25mm Length | Easy Fan Volume Lashes 2D-20D Self Fanning Volume Lashes 0.10CC Mix-8-15mm Long Lasting Blooming Lashes(0.10CC Mix8-15)
42. [All Beauty] SHANGXING 2 Pack Eyelash Holder Tray Mold with Lid- 2 Shapes Display Tray Resin Mold-DIY False Eyelash Holder Epoxy Storage Case for Making Cosmetic Case
43. [All Beauty] SUSSURRO 12 Rolls Eyelash Extension Tape  Eyelash Lash Tape for Lash Extension Breathable Adhesive Fabric Non-woven Wrap Lash Tape for Eyelash Extensions
44. [All Beauty] Sam&Helen 100% Handmade Siberian Mink Eyelashes | Blanche | Reusable 3D Mink Lashes for Daily Makeup Natural|Thick|Long|Short 8 Styles Options
45. [All Beauty] Teenitor 100pcs Glue Holder and Lash Organizer for Individual Eyelashes Volume Fan Building, Quick Blossom Cup for Sharpening or Closing Volume Fans Eyelash Extensions
46. [All Beauty] Volume Lash Extensions Thickness 0.07mm C Curl 12mm Rapid Blooming Easy Fan Mink Black|Thickness 0.05/0.07/0.10/0.12mm C/D Curl Length Single 8-18mm Mix-8-15mm Mix-9-16mm| (0.07-C-12mm)
47. [All Beauty] WEYZIM 3D Faux Mink Lashes 2 Pairs Handmade Luxurious Volume Fluffy Natural False Eyelashes Reusable 100% Handmade 3D02
48. [All Beauty] Waterproof Mascara, Lash Mascara Long Lasting, Smudge-Proof, Natural Thickening, Lengthening, Volumizing, Clump-Free Application, Black
49. [All Beauty] Y-KINZ Upgraded Invisible Magnetic Eyelashes and Eyeliner Kit False Lashes With Applicator Tool， No Magnet Block on Eyelashes Waterproof Long Lasting Reusable No Glue Needed[6 Pairs]
50. [All Beauty] wiwoseo False Eyelashes Faux Mink Lashes 7 Pairs Pack Dramatic Fake Eyelashes Long Fluffy Thick Crossed Eye Lashes Multipack

Return JSON only with this schema:
{
  "cluster_id": 9,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 10

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 10
Cluster size: 526

Representative product titles:
1. [All Beauty] 0lay Luminous Brightening & Protecting Lotion, SPF 30-1.7 Fl Oz (50 ml)
2. [All Beauty] 2016 NEW HERA UV MIST CUSHION ULTRA MOISTURE : SPF34/PA++#21 Vanilla 0.53oz(15g)+Refill 0.53oz(15g)
3. [All Beauty] 24K Gold Under Eye Patches Eye Masks For Dark Circles And Puffiness with lifting effect 20 pairs 40 pcs Revitalize and Refresh Your Skin
4. [All Beauty] Adelina Skin Cream 1.0 fl oz/30mL
5. [All Beauty] Baisidai Pack of 10/20/30/40 Pairs Collagen Crystal Eye Mask Eyelid Patch Deep Moisture Anti Wrinkle (10PCS, White)
6. [All Beauty] Beyond Deep Moisture Body Emulsion (200ml)
7. [All Beauty] CC CREAM OR ANTI-REDNESS MAGIQUE NUDE
8. [All Beauty] CLE Cosmetics CCC Cream Foundation, Color Control and Change Cream That's a BB and CC Cream Hybrid, Multi-purpose Beauty Primer and Facial Foundation for the Best Skin Ever, 1 fl oz SPF 50 (Warm Medium Deep)
9. [All Beauty] Celleral Anti-Aging Combo Celleral Anti-Aging Serum + Celleral Eye - Argireline, Matrixyl, Haloxyl, Hyaluronic Acid, Powerful Collagen Booster, BEST-SELLING WRINKLE TREATMENT + EYE TREATMENT COMBO!
10. [All Beauty] Cosmo Hurry Harry Collagen Serum Bar
11. [All Beauty] Danielle Laroche Eye Perfect Vitamin C Eye Serum 1 oz
12. [All Beauty] Drunk Elephant GLOWY – The Night Kit. Complete Evening Skincare Routine (Jelly Cleanser, Glycolic Night Serum, Micellar Water, Electrolyte Mask and Whipped Cream Moisturizer)
13. [All Beauty] Dsiuan Under Eye Patches,30 pairs Hyaluronic Acid Anti-Aging Under Eye Mask, Collagen Under Eye Gel Pads for Dark Circles, Wrinkles, Fine Line, Puffiness
14. [All Beauty] Everyday Beauty Age-Defying Eye Cream to Minimize Dark Circles, Discoloration, and Puffiness, Anti-Aging Eye Cream with Squalene and Hyaluronic Acid, 0.5 oz. Jar
15. [All Beauty] Facial Essence Mask, Firming & Lifting with Vitamin C (12 Count)
16. [All Beauty] Graydon Skincare - Natural / Non-Toxic Germs Away Mist (4 oz / 120 ml)
17. [All Beauty] Hale Cosmeceuticals Dermist M3 Hyaluronic Acid, 2 oz
18. [All Beauty] Hempz HydroKiss BB Facial Bronzer, 3.4 Ounce
19. [All Beauty] Honey Jarret Beau'tea Serum, With Centella Extract, Madecassoside, Panthenol, Facial Serum for Hydrating, Soothing, Brightening, 1.01 fl.oz
20. [All Beauty] Hyaluronic Acid Serum - Anti Aging and Firming Skin - Soothe and Nourish Face - Natural Ingredients with Aloe and Lavender Oil (1oz)
21. [All Beauty] IPKN Pore Apple Sunblock 70g SPF50+ PA+++
22. [All Beauty] L'Oreal Paris Age Perfect Cell Renewal Facial Oil, 1.0 fl oz
23. [All Beauty] L'Oreal Paris Age Perfect Hydra-Nutrition Facial Day Lotion SPF 30 (Pack of 2)
24. [All Beauty] LADY ESTHER 4-PURP FACE CREAM Size: 7.5 OZ
25. [All Beauty] LaClaire Skin Revitalization Clarifying Formula - Exfoliating Face Wash - Anti Wrinkle Face Wash – 1.9 % Salicylic Acid Exfoliating Cleanser - Smooth, Young & Radiant Skin – For Daily Use - 50mL / 1.7 oz, Made in the USA
26. [All Beauty] Lasting Makeup Foundation – Face&Body Liquid Foundation Lightweight Bottle Full Coverage Invisible Pores Covering Blemishes - for All Skin Types (40 mL)
27. [All Beauty] Lindsay Home Aesthetics Diamond Rubber Face Mask - Help Reduce the Appearance of Sun-Damaged Skin & Protect Skin - Smoothing, Brightening, Hydrating Skin Benefits, 2 Masks 5.04 oz
28. [All Beauty] Nature Republic Real Comforting Mask Sheet, 2 Sheet (Panthenol_Emulsion Type)
29. [All Beauty] Nigel Anthony ADVANCED COLLAGEN CREAM - Natural Facial Skin Care for Tightening, Wrinkles, Fine Lines & Younger Skin. For Men & Women
30. [All Beauty] ORIGINAL FORMULA Max Factor Pan-Cake Water-Activated Foundation Powder, 129 MEDIUM BEIGE
31. [All Beauty] Organic Vitamin C Serum for Face-Professional Strength-Organic Vitamin C Serum-Hyaluronic Acid-Vitamin E-Naturally Derived 20% Vitamin C The Best Vitamin C Serum (1 Ounce)
32. [All Beauty] PINEAPPLE & VITAMIN C SKIN BRIGHTENING CLEANSER: SKIN Rejuvenation, Anti-aging, Anti-wrinkle, Skin Hydration, Pineapple stem cell
33. [All Beauty] Parisian Secret Revitalizing Moisturizer
34. [All Beauty] Paul Scerri Hydrogel Moisturizing Compound 6.8oz, 200ml
35. [All Beauty] Protege FLAWless Scar Gel Cream, Best for Scar Removal, Flattens and Softens Scars (1 ounce)
36. [All Beauty] Retinol Gold Anti-Aging Serum with Hyaluronic and Collagen
37. [All Beauty] Reusable Silicone Face Patch Set - 5 Wrinkle Patches for Overnight Fine Line & Crease Flattening - Forehead, Under-eye and Smile Lines Repair
38. [All Beauty] SKINRx LAB Madecera Body Moisturizer Re-turn Series 200ml (6.76oz.) Body Lotion
39. [All Beauty] Skin Fetish Natural Sheet Deep Sea Collagen Facial Masks
40. [All Beauty] Skincare Retinol Skin Brighten Er 1oz (3 Pack)
41. [All Beauty] Skincare by thisworks In Transit Spray-On Moisture 100ml
42. [All Beauty] TIANG Facial Steamer, Nano Ionic Mist Face Steamer, Hydrating Mist Sprayer Water Oxygen Injection, Nano Steamer Portable Mist Humidifier, for Face Mini Spa Rejuvenation, Moisturizing Refreshing
43. [All Beauty] Transdermal C Balm by Benjamin Knight Fuchs R.Ph. Truth Treatment Systems, Vitamin C Skin Cream, Anti-Aging Transdermal Moisturizer for Dry Skin, Hydrating Cream Bright & Smooth Complexion (15ML)
44. [All Beauty] Under Eye Patches - Under Eye Mask for Dark Circles Collagen Eye Mask for Puffy Eyes Under Eye Bags Treatment Gold Eye Masks Skin Care Under Eye Pads
45. [All Beauty] VALITIC Foot Peel Mask for Dry Cracked Feet and Dead Skin Callus Removal - Vitamin E & A Aloe Vera Collagen Moisturizing Natural Korean Complex - Extra Strength - Men and Women 3 Pairs - Tea Tree
46. [All Beauty] Vitamin C Serum for Face with Hyaluronic Acid - Hydrating Brightening Tone Perfection Facial Serum for Anti Wrinkle, Anti Aging, Acne Skin Repair, Age Spots Corrector 1 fl oz
47. [All Beauty] Vivo Per Lei Vitamin C Night Cream - Brightening Night Cream Moisturizer for Fine Lines and Wrinkles - Vitamin C Moisturizer with Palm Oil, Green Tea, Vitamins A - Night Face Cream to Moisturize Skin
48. [All Beauty] Winky Lux Eye Cream Applicator, Eye Roller for Puffy Eyes for Boosted Circulation & Reduction of Fine Lines and Wrinkles
49. [All Beauty] Yes to Tomatoes Clear Skin Detoxifying Micellar Cleansing Water 7.77 oz.
50. [All Beauty] Youngblood Clean Luxury Cosmetics Natural Loose Mineral Foundation, Sable | Loose Face Powder Foundation Mineral Illuminating Full Coverage Oil Control Matte Lasting | Vegan, Cruelty Free

Return JSON only with this schema:
{
  "cluster_id": 10,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 11

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 11
Cluster size: 375

Representative product titles:
1. [All Beauty] 2 Makeup Brush Cleaning Mats,Silicone Makeup Brush Cleaner With Suction Cup,Portable Washing Tool Scrubber Pad For Brushes,Makeup Brush Cleaning Pad
2. [All Beauty] 6 Pieces Self Applicator Kit, Include Exfoliating Glove, Tanning Mitt, Bath Mitt, Mini Face Mitt and Back Lotion Applicators (Black Set)
3. [All Beauty] AIVOYE Blackhead Remover, Tearing style Deep Cleansing purifying peel off the Black head,acne treatment, black mud face mask 60g
4. [All Beauty] Anti Aging Jade Roller Therapy - 100% Natural Jade Facial Roller Double Neck Healing Slimming Massager - Real Jade Stone Roller with Double Head/Slim Face Stimulate Face - SkinCare Cold Stone Massage
5. [All Beauty] Aquis 4x30.75 Inch Linen Exfoliating Back Scrubber and 12x12 Inch Linen Exfoliating Washcloth
6. [All Beauty] Aunt Fannie's Microcosmic® Probiotic Power Cleaning Wipes 35 Count (Mandarin Grove)
7. [All Beauty] BICAMERAL Guasha Massage Stone (3 COUNT) - All Natural Premium Jade Therapy Tool – SPA Facial Treatment – Great for Smoothing Muscles and Tissues – Releases Toxins in Neck, Face, Skin, and Body – PR
8. [All Beauty] Baby Safety Cotton Swabs for Infant Baby Kid Ear Nose Clean White Cotton Double Tipped Natural Paper Sticks Spiral Head Multipurpose Cotton Buds Cleaning Sticks (M552)
9. [All Beauty] Bare Rush Garshana Gloves 100% Raw Silk Massage Gloves Ideal for Ayurvedic Massage, Dry Skin Brushing, Exfoliation, Cellulite Reduction, Unclogging Pores, Stimulating Your Lymphatic System
10. [All Beauty] Blackhead Remover Vacuum Blackhead removal tool Blackhead Vacuum,USB Rechargeable Face Vacuum Acne Comedone Extractor Tool Pore vacuum Cleanser Suction Tool with LED Display-Suction Force for All Skin
11. [All Beauty] Blackhead Remover with Camera, 20x Magnification Visual, Strong Suction with 5 Replaceable Probes, USB Rechargeable Pore Vacuum Pore Cleanser for Women Men
12. [All Beauty] CCbeauty 10Pcs Nose Blackhead Remover Strips 3-Steps Kit Nose Clear Face Cleanser Mask Peel Off Blackheads Pore (10 Pcs)
13. [All Beauty] Disposable Cotton Face Towel, HUANGHUIHAO Makeup Remover Towels Multi-Purpose Cotton Soft Facial Cleansing Towel Disposable Cotton Face Towel 80 Cotton Tissues
14. [All Beauty] Double-Cleansing Botanical Face Wash
15. [All Beauty] Face Cleanser Stick by Disco for Men, Hydrating, Removes Dirt and Build Up, All Natural and Paraben Free, Eucalyptus Scent, 2.12 Ounces
16. [All Beauty] Facial Cleansing Brush, Sonic Ultrasonic Vibration Facial Brush, Red-light for Deep Cleaning, Discharge Makeup, Gentle Exfoliating, Blackhead Removing, Massaging with 3 Adjustable Modes and Speeds
17. [All Beauty] GooMart 5 Pieces Silicone Makeup Sponge Applicator for Blending Liquid Foundation or Creams
18. [All Beauty] Green Tea/Eggplant Purifying Clay Stick Mask, Face Moisturizes Oil Control, Deep Clean Pore, Blackhead Remover Acne Deep Cleansing, Improves Skin for Women Men (Green Tea+Eggplant)
19. [All Beauty] Grteark 6 Pcs Makeup Sponge and Round Facial Sponge Two Uses, for Removing Dead Skin, Dirt and Makeup Foundation, Beauty Blender Sponge for Blending Liquid, Powders and Creams, Liquid Application
20. [All Beauty] Hetian Sonic Facial Cleansing Brush，Exfoliating and Waterproof Electric Face Wash Brush Deep Skin Care Tools Silicone Cleanser Scrubber Suitable for Any Skin Condition for Women (Red)
21. [All Beauty] KINGDOMCARES Steamer 3-in-1 Warm Mist Moisturizing Facial Steamer Face Steamer Humidifier Hot Mist Clear Blackheads Acne Facial Hydration Home Sauna SPA Skin Care Atomizer Pink
22. [All Beauty] Komost Dry Brush, Bamboo Shower Back Brush Long Handle, Body Back Scrubber for Shower for Men Women, Foot File Callus Remover for Dead Skin
23. [All Beauty] LANDWIND Face Roller Massager, Y-Shape 3D Roller for Anti Aging, Face Lift, Anti Wrinkles, Skin Tightening (BA311)
24. [All Beauty] Luxury Makeup Sponge Blender - Makeup Sponge Applicator For All Powder And Liquid Cosmetics - Flawless Look Every Day
25. [All Beauty] MLMSY Solid Depilatory Grain Body Hair Remover Hard Wax Beans Depilatory Pearl Hard Wax Granule Hot Film Wax Bean Stripless Depilatory Wax Bead … (S)
26. [All Beauty] MUJI Japan Sponge Powder Puff 4pcs
27. [All Beauty] Majestic Pure Makeup Remover for Eye and Face, Skin Cleanser, Lavender Micellar Water, 8 Fluid Ounce
28. [All Beauty] Makeup Brush Cleaning Mat, Makeup Brush Cleaner, Compact Makeup Brush Cleaning Mat, Cosmetic Brush Cleaner, Portable Makeup Brush Cleaner, Makeup Brush Scrubber,
29. [All Beauty] Mothers Day Gifts for Mom Jade Roller Face Massager - Ice Roller gifts for Girl, Women, Girlfriend, Wife, Mom - Christmas Gifts Face Roller Massage Tool - Derma Roller for Skin Care
30. [All Beauty] Natwag Makeup Remover Cloth 5 Pack -Reusable Microfiber Cleansing Towel，Suitable for All Skin Types，Move Makeup Instantly（5 pack）
31. [All Beauty] Nicole Miller 4 Pack Facial Cleansing Wipes (30 Count Each) , 120 Facial Cleansing Cloths, Removes Makeup, Mascara, Dirt and Oil (Retinol, Rose Water, Collagen, & Rosehip)
32. [All Beauty] No Absorbing Velvet Makeup Sponge, Latex Free Makeup Sponge Egg, Microfiber Beauty Blending Sponge, Flocking Makeup Sponge Set (3, Purple Velvet)
33. [All Beauty] OJYUDD 20 Pcs Soap Exfoliating Bag,Soap Mesh Bag with Drawstring
34. [All Beauty] Paradream Blackhead Remover Mask Peel Off Blackhead Mask Face Mask Valuable 4-in-1 Original Snail Repair Facial Serum & 4 Pimple Comedone Extractors & Recyclable Brush (4Packs)
35. [All Beauty] Reuseable Makeup Remover Pads 12 Pack Microfiber Face Cloth Facial Cleansing Towels Suitable for All Skin Types Face Cloths Multiple Colors
36. [All Beauty] SeroVital Super Saturated Restoring Cleansing Cloths - Cleansing Face Wipes with Green Tea and Hyaluronic Acid - Makeup Remover Wipes - 1 Pack 15 Ct
37. [All Beauty] Silicone Back Scrubber For Shower - Body Brush For Bathing - For Back Cleansing And Exfoliating, Back Massage, All Parts Of The Body To Remove Ash And Mud (grey)
38. [All Beauty] Silicone Back Scrubber for Shower, Long Bath Body Brush, Silicone Body Towel for Exfoliating, Cleansing, SPA & Massage, Upgrade Length to 31.8 inch More Suitable for Adults(Blue)
39. [All Beauty] Silicone Back Scrubber for Shower, Silicone Bath Body Brush Back Scrubber for shower for Men and Women, Easy to Exfoliating Scrub Body Back Massage Scrubber 35.4inch/90cm(Blue)
40. [All Beauty] Silicone Makeup Sponge 2 Pack Premium Quality Silisponge -Easy To Wash Beauty Sponge Applicator for Flawless Application of Liquid Foundation,Primer, Concealer by SEALUXE
41. [All Beauty] Silicone Sponge Applicator for Makeup and Tanning Lotion - Flawless Coverage for ALL Skin Types, Latex-Free, Non-Toxic
42. [All Beauty] Simple Cleansing Facial Wipes, Oil Balancing 25 ct
43. [All Beauty] Skin care makeup brush set Facial Mask mixing bowls for face mask acne treatment, Brush, Stick, Measure Spoon, bowl set 6 in 1
44. [All Beauty] Smith & Nephew Adhesive Remover RemoveWipe #403100
45. [All Beauty] Terviiix Volcanic Oil Absorbing Roller Facial Skin Care Tool Oil Control Stick, Pink
46. [All Beauty] Ulta Large Makeup Sponge Super Blender
47. [All Beauty] Wax Warmer Hair Removal Kit | Waxing Kit with 3 Hard Wax Beans and 10 Applicator Sticks | Professional and Home Wax Heater for Women and Men | Face | Body | Bikini Hair Removal
48. [All Beauty] Wax Warmer, WLWQ Hair Removal Wax Kit with Hard Wax Beans and 20pcs Wax Applicator Strips, Women Men Painless at Home Waxing Kit for Body Legs Eyebrows Face Bikini Area Armpit
49. [All Beauty] Waxing Kit Wax Warmer Wax Beads for Hair Removal waxing kit for Women, with 4 Packs Hard Wax Beans and 10 Wax Applicator Sticks(black)
50. [All Beauty] Wow Towels 5-Pack Makeup Remover Cloths, Lift Away Makeup and Dirt With Ease, Ultra Soft for Squeaky Clean and Tight Pores (White)

Return JSON only with this schema:
{
  "cluster_id": 11,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 12

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 12
Cluster size: 695

Representative product titles:
1. [All Beauty] 100% Real Human Hair Silk Base Top Hairpiece Clip in Topper Wig for Women Crown in Hand-made Toppee Middle Part with Thinning Hair Loss Hair #4 Midium Brown 10''20g
2. [All Beauty] 23" Anime Cosplay Wig Big Wavy Full Bangs Wig Top Quality Synthetic Japanese Heat Resistant Fiber+Free Elastic Weaving Wig Cap - Light Blue
3. [All Beauty] 5 Pcs U Part Wig Caps for Making Wigs - Lace Wig Cap with Adjustable Strap - Black Breathable Wig Making Caps for Women (U Part Wig Caps-B Style)
4. [All Beauty] 613 Full Lace Wig Human Hair With Baby Hair Blonde Full Lace Wig Pre Plucked Bleached Knots (18 inch, full lace wig)
5. [All Beauty] ALICE Blonde Lace Front Wig, 24" Long Natural Straight Middle Part Synthetic Full Wig for Women
6. [All Beauty] ALICE Lace Front Wigs Copper Orange Bob Wig, 14" Short Natural Straight Synthetic Full Wig for Women
7. [All Beauty] ANNIVIA Short Curly Wig with Bangs for Black Women 10Inch Afro Kinky Curly Wig No Glue Full and Fluffy like a Bomb (Black)
8. [All Beauty] Afro Kinky Curly Wigs Heat Resistant 100% Fiber Ombre Brown Synthetic Lace Front Fluffy Wigs for African American Women 20 inch
9. [All Beauty] Aliesencia Pastel Wavy Wig With Air Bangs Short Bob Wigs Shoulder Length Wigs Curly Wavy Women's Synthetic Cosplay Pastel Bob Wig for Girl Colorful Costume Wigs(12",Brown)
10. [All Beauty] Anogol Hair Cap+Long Wavy Lace Front Wig Copper Red With Free Part Long Curly Synthetic Lace Front Wig for Girls Copper Red Curly Wig Lace Front for White Women
11. [All Beauty] Baruisi 6 Pack Hat Stands,Portable Wig Hanger for Wig and Hat,Durable Collapsible Travel Wig Stands,White
12. [All Beauty] Baseball Hat Hair Extensions Baseball Cap With Hair Attached Wig With Hat Synthetic Curly Corn Cap Hair Extensions Wave Natural Black Hat with hair for Women #12P24 light brown mix ash blonde
13. [All Beauty] Beweig Short Curly Red Wigs Afro Wig for Black Women Fluffy Synthetic Heat Resistant Halloween Cosplay Party Full Wig
14. [All Beauty] CTRLALT Short Wavy Wig Blonde 6 Inch Synthetic Short Black African Wig Suitable For Black Women Black Blonde Mixed Brown Heat Resistant
15. [All Beauty] Chantiche Soft Curly Glueless Lace Front Wigs Human Hair with Baby Hair for African Americans Natural Looking Brazilian Remy Hair Full Wig for Black Women 14 Inches Natural Black #1B
16. [All Beauty] Chu Yao 4 Inch Short Afro Kinky Curly Wigs Synthetic Afro Wigs for Women Black synthetic fiber braided hair short curly wig Give You Beautiful Looks
17. [All Beauty] Civrie Ash Blonde Short Wavy Bob Wigs for Black Women, Synthetic Ombre Grey Wig with Bangs Heat Resistant Natural Looking Cosplay Wig for Women
18. [All Beauty] ColorGround Dyed Dark Root Blonde Wig With 6 Ear Clips Necklace and Mustache for Men
19. [All Beauty] Colorful Bird Straight U Part Human Hair Wig for Black Women Ombre  10A Brazilian Remy Virgin Hair U Part Clip in Half Wig with Straps and Combs (1b/30, 16 inch)
20. [All Beauty] DEEKA 12" Straight Women's 2 Tones Brown and Silver Gray Ombre Wig Heat Resistant Fiber Synthetic Wigs+Wig Cap+Wig Comb
21. [All Beauty] EastHair Short Straight Hair Bob Wig Ombre Brown Wig 13'' with Bang Nature Synthetic Wig Straight Hair for Women (R1B/30)
22. [All Beauty] Ebingoo Pink Natural Wave Long Synthetic Lace Front Wig For White Women 24 inch
23. [All Beauty] FASHION PLUS Body Wave Human Hair Wigs with Bangs 150% Density None Lace Front Wigs Glueless Machine Made Human Hair Wigs for Black Women Natural Color (20 inch)
24. [All Beauty] Finders Wigs For Women Short Curly Wigs Highlights Black White Wigs Heat Resistant Synthetic Wigs For Elderly Women 14Inch
25. [All Beauty] GIANNAY Long Straight Glueless Lace Front Wigs for Women Heat Resistant Fiber Synthetic Hair with Baby Hair 24 inch 13x2.5 Inch Lace
26. [All Beauty] HANNE Kinky Curly Black Headband Wigs for Women Afro Curl Glueless Soft Hair None Lace Coily Head band Wig (Black)
27. [All Beauty] HMD Ombre Red Wigs for Women 30 Inches Long Straight Wigs Middle Part Wigs for Daily Cosplay Wear(Color: Ombre Red)
28. [All Beauty] Headband Wig Straight Hair 14 inch Human Hair Headband Wigs for Black Women Brazilian Virgin Hair 150% Density Glueless None Lace Front Wigs Natural Color
29. [All Beauty] Headband Wigs for Black Women Human Hair Kinky Curly Head Band Wig Brazilian Glueless None Lace Front Curly Wigs 150% Density
30. [All Beauty] Human Hair Lace Front Curly Wigs Black Real Remy Hair Water Wave Wig for Black Women Free Part 360 Lace Frontal Pre Plucked Glueless Natural Hairline with Baby Hair 150% Density 24 Inch
31. [All Beauty] Human Hair Wigs Bob Lace Front Wig,T Part Straight Short Bob Lace Wigs for Women Middle Part 13x6x1 Pre Plucked with Baby Hair Swiss Lace 12 Inch
32. [All Beauty] Jolanly Headband Wigs for Black Women Body Wave Human Hair Wigs Brazilian Virgin Human Hair No Gel None Lace Front Wigs With Headband Machine Made Wigs Headband Wig Scarf Wigs 150% Density 24 Inch
33. [All Beauty] Kinky Curly Headband Wig for Black Women,Long Natural Black Wave Curly Wigs with Headband Attached Deep Wave Wig Easy to Wear Machine Made Head Wrap Wig for Black Women Headband Wig Curly (20 Inch)
34. [All Beauty] Lace Front Human Hair Wigs Pre Plucked Hairline Bleached Knots 150% Density Brazilian Body Wave Lace Front Wigs Natural Color (22 inch, 150% Density 4x4 Wigs)
35. [All Beauty] Lace Front Wig Human Hair Straight Wigs for Black Women, 4x4 Brazilian Virgin Human Hair Lace Closure Wigs, 150% Density Straight Human Hair Wigs Pre-Plucked with Baby Hair Natural Color (16 Inch)
36. [All Beauty] Long Wave Women Wig with Hats Synthetic Dark Brown Corn Wavy Wigs with Baseball Cap Baseball Hats with Hair Hair Pieces Hair Extension for Women (Dark Brown)
37. [All Beauty] Miss Elegant 22'' Hairpieces Hidden Invisible Wire in Synthetic Hair Extension Not Clip in Hair Extensions Secret Miracle Wire Hair Piece with Fish Line Headband Long Curly Wavy Hair (Black/Wine Red)
38. [All Beauty] Monikahair Headband Wig Long Straight Natural Black Wigs for Black Women Glueless 28inch Headband Wig Natural Looking Synthetic Half Wigs for Black Women Daily Party
39. [All Beauty] NAKED UNPROCESSED REMY HUMAN HAIR INVISLBLE L-PART LACE FRONT WIG - BODY WAVE
40. [All Beauty] SUNYUON Lace Front Wigs Human Hair Body Wave 13x4 HD Lace Frontal Wig Pre Plucked with Baby Hair Brazilian Lace Front Wig Human Hair Wigs for Women 150% Density Natural Black Color（18inch）
41. [All Beauty] Sensationnel lace front wig - custom lace wig perm romance
42. [All Beauty] Short Headband Wigs for Black Women Afro Kinky Curly Wigs Head Wrap Wig 2 in 1 Wig Synthetic Natural Black Wigs with Bangs Short Curly Wigs with Headband (Leopard Turban Wig)
43. [All Beauty] Stamped Glorious Long Corn Wave Ponytail Extension Magic Paste Heat Resistant Wavy Synthetic Wrap Around Ponytail Black Hairpiece for Women (22inch, 111)
44. [All Beauty] Stamped Glorious Short Wavy Bob Wig Synthetic Wine Red Color Wigs with Bangs for Women Shoulder Length Heat Resistant Fiber Wigs (Burgundy)
45. [All Beauty] Superhairpieces Men's Toupee NM101 Premium Natural Indian Remy Hair 0.2mm 8"x10" Super Clean PU Thin Skin Hairpiece Mens Human Wigs Toupee for Men (Brown Black)
46. [All Beauty] SureWells Costume Wigs Uta no Prince SAMA Shining Orange Wigs Cosplay Wigs Party Wigs Costume Wigs
47. [All Beauty] Wig
48. [All Beauty] Yupher Synthetic Brown Wig with Bangs for Black/White Women (242-5)
49. [All Beauty] ZILING Headband Wig Human Hair Body Wave Headband Wigs for Black Women Glueless None Lace Front Wigs with Headband Attached 150% Density Half Wigs Natural Color 16 Inch
50. [All Beauty] Zury Sis Deep& Wide Pre-Tweezed Part Synthetic Wig NAT-H 3A JAMAI (FS1B/30)

Return JSON only with this schema:
{
  "cluster_id": 12,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 13

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 13
Cluster size: 341

Representative product titles:
1. [All Beauty] 2 PCS French Smile Line Cutter for Nails, Stainless Steel C Shape V Line Edge Trimmer Templates for DIY Plate Module Gel Cutter Tool
2. [All Beauty] 2 Pieces Multifunctional Toothpick Double Ended Stainless Steel Toothpicks Portable Dental Tools Cleaning Tools Kit Stainless Steel Dental Scaler Pick Hygiene Plaque Remover
3. [All Beauty] 240 Pieces Earrings Hole Cleaner, 4 Boxes Disposable Earrings Hole Cleaning Line Odor Removal Ear Care Kit For Girls Women Men
4. [All Beauty] Active Wow Charcoal Teeth Whitening Powder + Toothpaste Bundle
5. [All Beauty] Andis T-Outliner Blackout Replacement Blade
6. [All Beauty] BIC Hybrid Advance 3 Disposable/System Shaver for Men, 6 Count
7. [All Beauty] Brush Cleaner 120 Ml
8. [All Beauty] Butler Floss Mate Handle - 845R - Pack of 6 - Assorted colors (Blue, Red or Both)
9. [All Beauty] Callus Remover,Bienna Electronic Foot File Pedicure Tools [Rechargeable] [Waterproof] Electric Professional Shaver for Dry Dead Cracked Hard Feet Skin Calluses with LED Light and a Extra Grinding Head
10. [All Beauty] Cibo Baby Infant Gentle Vibrations Toothbrush LED Lights Child Electric Sonic Toothbrush with 3 Brush Heads (Green)
11. [All Beauty] Colgate Total Professional Medium Full Head Toothbrush - 1 ea
12. [All Beauty] Cordless Water Dental Flosser,Portable Dental Oral Irrigator Teeth Cleaner ,Portable Oral Irrigator for Deep Teeth/ Braces Cleaning ,Chargeable IPX7 Waterproof for Home Travel (White)
13. [All Beauty] Crystal Twin Blade Plus Disposable Razors Lubricating Strip (Compatible)
14. [All Beauty] Dermasoft Bucket End Tragus Body Forceps
15. [All Beauty] Double Edge Razor Blade Sample Pack For Beginners (2x each)
16. [All Beauty] Electric Foot Callus Remover, Rechargeable Feet Callous removers, 3 Grinding Heads Portable Waterproof Foot File, Professional Pedicure Tools Feet Care for Dead, Hard Cracked Dry Skin-Black 1200mAh
17. [All Beauty] Electric Toothbrush, 150 Days Use Rechargeable 8 Heads for 2 Years, IPX7 4 Modes Electric Toothbrush for Adults, OGuard Smart Toothbrush, Ultra Clean Sonic Toothbrush with Travel Kit 2 Mins Timer
18. [All Beauty] H2ofloss Water Flosser Professional Cordless Dental Oral Irrigator - Portable and Rechargeable IPX7 Waterproof
19. [All Beauty] HQ8 SH50/52 Shaving Heads for Norelco Replacement Electric Shaving Head Razor Blades （3 pack）
20. [All Beauty] Haryali London 3 Edge Shaving Razor With Black Coated Handle Beard and Mustache Safety Razor For Men and Women
21. [All Beauty] Heel Smoother Pro Replacement Tips
22. [All Beauty] Hot Tools Blowout Round Brush With Sectioning Pik
23. [All Beauty] Ion Magnesium Flexible Vent Brush
24. [All Beauty] Jaw Exerciser for Men and Women - Jawline Double Chin Reducer Eliminator - Chisell Jawline Exerciser - Powerful Chisel Jaw Trainer
25. [All Beauty] King Head Deep Clean Toothbrush 4 Pack with Mugwort Infused Medium Bristles for Cleaner, Whiter Teeth and Fresher Breath, Large Ergonomic Head for Proper Dental Care
26. [All Beauty] LED Lighted Scaler with dental Mirror, stain remover oral hygience
27. [All Beauty] LaCross Shears
28. [All Beauty] Laxcare Water Flosser, Cordless Teeth Cleaner Rechargeable Portable Oral Irrigator with 3 Modes, IPX7 Waterproof Dental Flosser with 2 Replaceable Tips,Detachable Water Tank for Home Travel, Cyan
29. [All Beauty] MAX-T Electric Shavers for Men, Wet & Dry Men's Electric Shaver, Cordless with USB Rechargeable and Pop-Up Trimmer, IPX7 Waterproof Electric Razor for Men,Best Foil Razor Gifts for Men
30. [All Beauty] MEHAZ Professional Acrylic Nipper MCO444
31. [All Beauty] Nose-Hair-Trimmer Eyebrow-Trimmer Painless-Facial-Hair-Trimmer-for-Men-and-Women USB-Rechargeable-with-Built-in-LED-Light
32. [All Beauty] Oral Irrigator Portable Dental Water Flosser Cordless IPX7 Waterproof Rechargeable Irrigator - Best Dental Care Flossing WaterJet - 3 Water Pressure Modes – 2 Replacement Nozzles for Home and Travel
33. [All Beauty] Oxygen Injection Machine, Professional Oxygen Deep Moisturizing Facial Machine Mini Household Air Compressor Airbrush Set Oxygen Sprayer Skin Rejuvenation Nano Spray Machine(Black)
34. [All Beauty] Philips Sonicare HX8012/30 Airfloss Replacement Nozzles
35. [All Beauty] RQ11 Replacement Heads Fit for Norelco SensoTouch 2D Shavers,1150x, 1160x,1170x,1180x,Easy To Replace,Upgrade OEM Blades，2 head
36. [All Beauty] Shaving Factory Blade Dispenser
37. [All Beauty] Shaving Razor Replacement Head for Philips Norelco SH50/52 S5000 S5010 S5380 S5570 S5571 S5420 Shaving Head Cutter
38. [All Beauty] Sonic Electric Toothbrush, USB Rechargeable Toothbrush, Adult Electric Toothbrush With Holder and 2 Replacement Heads
39. [All Beauty] Stand Electric Toothbrush Heads Case Holder for Braun Oral B
40. [All Beauty] T Blade Trimmer, Electric Hair Clippers for Men, Professional Cordless Outliner Hair Trimmer, USB Rechargeable Hair & Beard Trimmer, Zero Gapped Detail Beard Shaver
41. [All Beauty] TRTK/B Magnetic Touch Knife-Blue
42. [All Beauty] Taylor Of Old Bond Street Platinum Brush, Platinum Shaving Cream Bowl 150g & Platinum Fragrance 50ml Set
43. [All Beauty] Tongue Scraper(2 Pack) for Oral Hygiene, Medical Grade Stainless Steel Tongue Scapers for Kids, Get Rid of Bad Breath and Halitosis, Tongue Cleaner with a Metal Case by IDOLUSTER(SPOON KIT)
44. [All Beauty] UniForU Jaw Exerciser,Jaw Exerciser for Women and Men, 4PC Face Toning Exerciser with Lanyard, Slim and Tone Your Face
45. [All Beauty] WANGDEFANG Dog Paw Cleaner, Dog Cat Paw Washer, Quickly and Effectively Clean Muddy Pet Paws Small (Red)
46. [All Beauty] WYZworks Wooden Luxury 3 Piece Oak Shave Kit Badger Brush Shaver Hanger Gentleman Set Compatible for Gillette Mach3 Razor
47. [All Beauty] Water Flosser
48. [All Beauty] Water Flosser Cordless,Dental Oral Irrigator :3 Modes 7 Jet Tips,IPX7 Waterproof,USB Charged 5 Hrs for 50-Days Use,Portable Water Picks for Teeth Cleaning for Home,Travel,Braces,Bridges,Care
49. [All Beauty] bqw 3 Blade Cartridge Razor Stainless Steel Handle for Mach3 Cartridges with Razor Stand
50. [All Beauty] co2crea Hard Travel Case for Philips Norelco Men Shaver Razor 3100 4100 2300 3500 2500

Return JSON only with this schema:
{
  "cluster_id": 13,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 14

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 14
Cluster size: 442

Representative product titles:
1. [All Beauty] 2 oz, Light Yellow - Bargz Perfume - True Religion Body Oil For Women Scented Fragrance
2. [All Beauty] 3 Narciso Rodriguez L'Absolu For Her EDP Women Spray Sample Vial 0.8 ml/0.02 oz
3. [All Beauty] 3-Pack Rose Vanilla Natural Deodorant Stick, 2.65 oz
4. [All Beauty] 316L Bike Essential Oil Diffuser Aromatherapy Locket Necklace
5. [All Beauty] AERIN 'Lilac Path' Eau de Parfum Spray 0.07oz/2ml Carded Vial by AERIN
6. [All Beauty] AXE Antiperspirant Deodorant Stick Phoenix 2.7 oz (Pack of 10)
7. [All Beauty] AXE White Label Dry Spray Antiperspirant for Men, Signature Forest 3.8 oz
8. [All Beauty] Aromatherapy Essential Oil Diffuser, 500ml Super Quiet Aroma Humidifier, Water Auto off, Sleep Night Light for Home Office
9. [All Beauty] Aussie Sprunch Aerosol Hair Spray Flexible Hold 10 oz (Pack of 3)
10. [All Beauty] Avon Black Suede SPORT 3.4 Fl Oz Eau De Toilette Spray LOT OF 2 sealed sold by The Glam Shop
11. [All Beauty] Bath and Body Works - Confetti Daydream - Gift Set - Fine Fragrance Mist & Body Cream
12. [All Beauty] Britney Spears Rocker Femme Fantasy Eau de Parfum 1.7oz (50ml) Spray
13. [All Beauty] Brut Hydrating Body Wash 360 Degree Deodorizing Protection Brut Revolution Fragrance 13 Oz. (1 Each)
14. [All Beauty] CLINIQUE AROMATICS ELIXIR EAU DE PERFUME 100ML VAPO. 75ML + BODY MILK + ELIXIR 6ML
15. [All Beauty] Christian Siriano People Are People Perfume Spray 3.4 fl oz / 100 ml EDP
16. [All Beauty] Clive Christian No. 1 Perfume Spray for Women 1.6 oz
17. [All Beauty] Commodity Moss Eau De Parfum Spray Unisex 3.4 oz / 100 ml Brand New Item In Box Sealed
18. [All Beauty] DEVROM® 200mg Capsules (Internal Deodorant)- 100 Capsules
19. [All Beauty] Dana English Leather Black For Men Cologne Spray 3.4 oz
20. [All Beauty] Degree Men Fresh Deodorant, Ever Fresh 3 oz (Pack of 4)
21. [All Beauty] Diptyque ILIO Eau de Toilette Spray 3.4 oz
22. [All Beauty] Disney Planes Mini Gift Set with 4 Miniature Eau De Toilettes
23. [All Beauty] Diva By Emanuel Ungaro For Women. Body Lotion 6.8 Oz.
24. [All Beauty] Dove Advanced Care Anti-Perspirant Deodorant, Revive 2.6 oz (4 Pack)
25. [All Beauty] ELSHA Perfume Redolence Women - Original Manufacturer of ELSHA PERFUME AND COLOGNE - the aristocrat of perfume and cologne [attract men]
26. [All Beauty] EXTREME INTENSE L'BEL Eau de Toilette Atomiseur Pour Homme
27. [All Beauty] Ellen Tracy Makeup Setting Spray Long Lasting Primer, Hydrating Face Mist, Dewy Setting Spray, Prep and Set Makeup - 8.4 Fl. Oz. Spray Bottle
28. [All Beauty] Essential Oil Diffuser Ultrasonic Cool Mist Humidifier Aromatherapy Aroma Diffusers Humidifiers Wood Waterless Auto Shut-Off for Baby Office Home Bedroom
29. [All Beauty] Estee Lauder 'Sensuous Sensual' Duo
30. [All Beauty] Feulover-Bitter-Apple-Spray-for-Dog-to-Stop-Chewing, No Chew Spray for Dogs, Pet Corrector Spray for Dogs&Cats, Stop Chewing Licking and Biting, Nontoxic
31. [All Beauty] Flavor Plus Oral Suspending Vehicle 16 oz
32. [All Beauty] Guess Dare Gift Set 1.0oz (30ml) EDT Spray + 2.5oz (75ml) Body Lotion
33. [All Beauty] Hayat Pure Concentrated Perfume Oil 12 ml / .40 oz Attar (Ittar) For Women Alcohol Free Fragrance By Hamidi (Hayat)
34. [All Beauty] I.D. - L'BEL - Eau de Toilette Colonia 100 ml e (3.4 fl.oz) UNISEX
35. [All Beauty] JANET COLLECTION BRAZILIAN SCENT PRE TWEEZED WIG - EMOTION (OET1B/30)
36. [All Beauty] La Perla - La Mia Perla - Eau De Parfum Spray 3.4 Oz
37. [All Beauty] Light Blue Swimming In Lipari/D&G Edt Spray 4.2 Oz (125 Ml) (M)
38. [All Beauty] Listerine Cool Mint Antiseptic Mouthwash, Bad Breath, Plaque & Gingivitis, Mint, 1.5 L (Pack of 3)
39. [All Beauty] Musk Tahara (White Musk) 12mL | Perfume and Body Oil from Fragrance House Swiss Arabian, Dubai UAE | Original Misk Blend | Alcohol Free and Vegan
40. [All Beauty] Natura Seve Oil Rosas Champagne Refill (Champagne Roses) 200ml
41. [All Beauty] Nest Fragrances New York Citrine Eau de Parfum Rollerball 0.1 oz Mini UB
42. [All Beauty] Oud Laki 100mL, a Light Unisex Eau de Toilette with sultry Amber and Patchouli by perfume artisan Swiss Arabian
43. [All Beauty] Pherone Formula M-11 Pheromone Cologne for Men to Attract Women, with Pure Human Pheromones
44. [All Beauty] Puroma Adjustable Aromatherapy Essential Oil Diffuser Wood Grain Fragrance Diffuser Cool Mist Humidifier with Waterless Auto Shut-Off Function and 4 Timers for Home Office Baby Room (White)
45. [All Beauty] ROYCE BLUE EAU DE PARFUM 3.4 FL OZ
46. [All Beauty] Rexona Body Roll on Deodorant for Men, Anti-Perspirant/Anit-Transpirant (3X50ml/1.7oz, Mix within the available kinds)
47. [All Beauty] Taste Beauty L.O.L. Surprise! 12 Scented Bath Bombs
48. [All Beauty] The Dry Look For Men Aerosol Hairspray Extra Hold 8 oz (Pack of 7)
49. [All Beauty] Victoria's Secret Love Addict Fragrance Set - Love Addict Lotion Love Addcit Fragrance Mist
50. [All Beauty] Zest Family Deodorant Bars, Whitewater Fresh 4 oz - 8 Bars

Return JSON only with this schema:
{
  "cluster_id": 14,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 15

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 15
Cluster size: 419

Representative product titles:
1. [All Beauty] !SALE! SUPPLY Tallow Shave Soap (Juniper, 4.5 oz)
2. [All Beauty] Almond Natural Soap (4 Bars)
3. [All Beauty] Ayumi Sandalwood & Ylang Ylang Face Wash. Vegan, Cruelty-Free, Dermatologically-Tested, 1 x 150ml
4. [All Beauty] Baby Bear Sensitive Baby Wipes - Unscented, 99% Water, Plant Based, Soft and Gentle, Made in the USA - 60 Count, Pack of 12
5. [All Beauty] Bath & Body Works Decorative Hand Soap Ripe Raspberry Vine
6. [All Beauty] Bath & Body Works Deep Cleansing Hand Soap White Lily & Lime 8oz
7. [All Beauty] Bath & Body Works LITTLE BLACK PARTY DRESS Duo Gift Set - Fine Fragrance Mist - Ultra Shea Body Cream
8. [All Beauty] Bath & Body Works Warm Vanilla Sugar Very Merry Wrapped Gift Set - Body Cream & Fragrance Mist
9. [All Beauty] Bath & Body Works, Signature Collection Body Lotion, Vanilla Bean Noel, 8 Ounce
10. [All Beauty] Baylis & Harding Pink Magnolia & Pear Blossom 300ml Hand Wash- Pack of 6
11. [All Beauty] Bien-etre Eau de Lavande Naturelle 250 ml
12. [All Beauty] Blood Orange Bergamot 4oz Certified Organic Soap Bar by Witch Hippie
13. [All Beauty] Bundle of 2 Assorted T.S. Pink SoapRocks (Bundle of Opal & Jade)
14. [All Beauty] CYMBOPOGON SOAP BAR with NO PRESERVATIVES - (Lemongrass Oil, Rice Bran Oil, Coconut Oil, Palm Oil), 2 x 3.5
15. [All Beauty] Caria Natural Soap Moisturising Olive and Wild Pistacia Oil Soap Bar (Bittim/Menengic). Natural Face, Hands & Body Wash. Softens & Nourishes Skin. Castile Traditional Vegan Handmade in Turkey (3 bars)
16. [All Beauty] Cherry Vanilla Float GFHS 2020 Gentle Foaming Hand Soap
17. [All Beauty] Crayola Bathtub Fingerpaint Soap,Colors May Vary 6 oz (Pack of 6)
18. [All Beauty] Crimson & Oak Body Wash for Men- Nourishing Gel Body Wash in Citron and Mint- by Body Prescriptions
19. [All Beauty] Dead Sea Collection Mineral Body Lotion with Cherry Blossom to Relax and Pamper 16.9 fl. oz.
20. [All Beauty] Dial Glycerin Soap, Pura Fruta. Refreshing Guava and Watermelon Scent. (Pack of 10 4 Ounce Bars)
21. [All Beauty] Dr. Woods Natural Pure Castile Bar Soaps made with Moisturizing Organic Shea Butter, 5.25 Ounce Bars Variety 9 Pack
22. [All Beauty] Elmore Mountain Farm Goat's Milk Soap - Lemongrass
23. [All Beauty] Fa Shower Cream - Yoghurt Vanilla Honey for Dry Skin 250ml/8.4oz
24. [All Beauty] Huggies Simply Clean Fresh Scented Baby Wipes Soft Pack (Packaging May Vary)
25. [All Beauty] Hyber&Cara Turquoise Soap Rock 75g Lily of the Valley Scented December Birth Stone
26. [All Beauty] Iconikal Jumbo 125g Loofah Bath Sponge, Random Colors, 2-Pack
27. [All Beauty] Indigo Wild Favorites Zum Bar Goat's Milk Soap, 3 Oz. Each: Frankincense & Myrrh, Tangerine-Orange, & Cedar
28. [All Beauty] J.R. Watkins Liquid Hand Soap, Desert Rose, 11 Ounces
29. [All Beauty] LEAP Lemongrass Hand Soap, Natural & Moisturizing Lather, Gentle & Rinses Clean, Made with Organic Oils, Cruelty Free & Vegan, Liquid Hand Wash, Superbly Designed, 12 fl oz
30. [All Beauty] Lux Velvet Touch Soap 4x100gm Buy 4 Get 1
31. [All Beauty] Melaleuca the Gold Bar - Citrus Scent Facial Soap
32. [All Beauty] Michel Design Works Large Bath Soap Bar - Confetti
33. [All Beauty] Michel Design Works Large Bath Soap Bar - Garden Melody
34. [All Beauty] Nivea Powerfruit Shower Gel, 250ml (Pack Of 2)
35. [All Beauty] Pacha Soap Company Spearmint Lemongrass 4 Oz. Natural Soap
36. [All Beauty] Patchouli Orange Shampoo Bar
37. [All Beauty] Pecksniffs Freesia and Poppy Moisturizing Shower Gel 33.8 Oz
38. [All Beauty] Plantanicals Charcoal & Bamboo Detoxifying Body Wash
39. [All Beauty] SHEA MOISTURE SOAP,MEN'S UTILITY, 5 OZ
40. [All Beauty] Sanctuary Body Lotion
41. [All Beauty] Set of 2: HARRY'S Men's Shave Cream 3.4oz - and Post Shave Balm - 3.4oz
42. [All Beauty] Shower Bombs! 5 Pack Aromatherapy Shower Steamers - Peppermint
43. [All Beauty] Simple Cleanser, Foaming 5 Ounce (2 Pack)
44. [All Beauty] Soap for Geeks - BEST SELLER! 6 oz Soap by Whiskey River Soap Co.
45. [All Beauty] Softsoap Limited Edition Blossom Breeze Body Wash Pack of 2 Bottles
46. [All Beauty] The Healing Garden Cleansing Body Wash - Uplifting Jasmine: 6.4 OZ
47. [All Beauty] Webat Bath Bombs Gift Set, Spa Bomb Fizzies & Ultra Lush Essential Oil - Dry Skin Moisturize, Fit for Bubble & Spa Bath, Handmade Birthday Gift Ideal for Lady, Women, Girlfriend, Men
48. [All Beauty] Yardley London Jasmine Pearl Bar Soap, 4.25 oz (Pack of 4)
49. [All Beauty] Zen Dairy Applejack Goat Milk Soap
50. [All Beauty] tamarinda Olive Glycerin Facial Soap - Two 5.25 oz. bars.

Return JSON only with this schema:
{
  "cluster_id": 15,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 16

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 16
Cluster size: 705

Representative product titles:
1. [All Beauty] 2 Pack J. Cat #MOTD Waterproof Slide On Lip Liner 106 Warm Brown by Jcat Beauty
2. [All Beauty] 2 Pack L.A. Girl Pro Conceal 992 Green Corrector
3. [All Beauty] 6 Pack Glitter Liquid Eyeshadow -High Pigmented Diamond Glow Shimmer & Metallic,Metals Foil Chameleon Quick Dry Crease Resistant Long Lasting Non-Greasy Eyeshadow
4. [All Beauty] Bite Beauty Glace Matte Creme Lip Crayon .031 oz Deluxe Sample Size Nib
5. [All Beauty] Bitzy Matte Lipstick Crayon 129 Perfect Pout
6. [All Beauty] Black Radiance True Complexion Soft Focus Finishing Powder, Milk Chocolate [9203] 0.45 oz (Pack of 12)
7. [All Beauty] Caboodles Flirty Makeup Train Case (Pink Plaid)
8. [All Beauty] Clé de Peau Beauté The Mascara, Black, 7ml/.22oz
9. [All Beauty] Colourpop Super Shock Glitter Sheer Eyeshadow (Paisley)
10. [All Beauty] Cruelty-Free and Talc-Free, Translucent Loose Face Setting Powder: Elizabeth Mott Set for Life Finishing Powder - No Color Baking Makeup for Oily Skin - Shine Control Matte Beauty Make Up Powder for Light Skin Tones - 15g
11. [All Beauty] Designer Skin Awestruck Tan Extender 16 oz
12. [All Beauty] FanMin Shimmer Lip Gloss Metal Lipstick,Primers Waterproof Moisturizing Liquid Lipstick,Long Lasting Glitter Lip Tints (02)
13. [All Beauty] Harmony Gelish - Forever Marilyn Fall 2019 Collection - Pick Any Shade .5oz (1110354 - All American Beauty)
14. [All Beauty] Herbivore - Natural Coco Rose Lip Polish | Truly Natural, Clean Beauty
15. [All Beauty] IT Cosmetics Pillow Lips Lipstick, Humble - Nude Cinnamon with a Cream Finish - High-Pigment Color & Lip-Plumping Effect - With Collagen, Beeswax & Shea Butter - 0.13 oz
16. [All Beauty] Jamila Henna Powder, 3.52-Ounce Box, 100 gms, 1 Pack
17. [All Beauty] Kat Von D Shade Light Crème Contour Palette
18. [All Beauty] L'Oreal Paris Mega Volume Collagen Miss Manga Mascara (INDIGO)
19. [All Beauty] Lime Crime Wet Cherry Lip Gloss, Potion - Red Orange Sparkle - High Shine, Non-Sticky Gloss - Cherry Scent - Lightweight Ultra Glossy Sheen - Won't Bleed or Crease - Vegan - 0.1 fl oz
20. [All Beauty] Lip Plumper Set, Ginger Mint Lip Enhancer and Lip Care Serum, Lip Mask, Fuller Lip, Moisturizing Lip Plumper Day/Night Set
21. [All Beauty] Lip Shape Lipstick, Cosmetic Makeup Tool 12 Colors Long Lasting Moisturizing Lip Gloss Lip Stick for Lazy Person
22. [All Beauty] MARC JACOBS Enamored Hi Shine Lip Lacquer Gloss 382 SUGAR High
23. [All Beauty] Mac Eye Shadow Eye color 1.5g Concrete
24. [All Beauty] Makeup Geek Foiled Eyeshadow (Blacklight)
25. [All Beauty] Manna Kadar Beauty Lip Locked Priming, Gloss Stain
26. [All Beauty] NYC Expert Last Lipcolor - Love My Latte
27. [All Beauty] Ownest 3 Pcs Avocado Moisturizer Lipstick,Natural Avocado Extract Moisturizing Lipstick Magic Color Change Lipstick Waterproof Long Lasting Lip Balm Lip Care
28. [All Beauty] PAT McGRATH LABS Skin Fetish: Divine Powder Blush Divine Rose
29. [All Beauty] Pack of 2 Maybelline New York Brow Drama Shaping Chalk Powder, Blonde 100
30. [All Beauty] Perfectly Posh Caffeinated Lip Balm - 0.10 oz / 2.95 g - You Pick Your Flavor! (Lemon Wedgie(Sweet Lemon Chiffon))
31. [All Beauty] Pixi Sheer Cheek Gel - No.4 Flushed - 0.53 oz
32. [All Beauty] Professional 120 Colors Warm Shimmer MakeUp Eyeshadow Palette (# 6 Color)
33. [All Beauty] Pure Vie Pro 5 Colors Cream Concealer Camouflage Makeup Palette Contouring Kit
34. [All Beauty] RIRE Triple Shading 9.5 Gram, Triple Color Facial Contouring Natural Figment Micro Powder Smooth Expression
35. [All Beauty] STAYVE BB Glow Starter Kit Pigments All Shades 12 vials
36. [All Beauty] Snaps, Genuine Italian Brown Leather" Chapstick Lip Balm Holder, MADE IN THE USA
37. [All Beauty] Strictly Black By Devoted Creations One-of-a-kind Super Charged Black Bronzer 12.25 Ounce
38. [All Beauty] TARTE Precious Picks Color Set: Amazonian Clay 12-Hour Blush in Ornate (rosy coral), Color Splash Lipstick in Surf’s Up (mauve), Lights, Camera, Lashes 4-in-1 Mascara (black)
39. [All Beauty] Tattoo Lipstick, Nature Nation 20 Pieces/Box Cotton Swab Lipstick Long Lasting Waterproof, Portable Kiss-proof Liquid Lip Glaze, Moisturizing with Natural Ingredients for Ladies(Color: Red/Multiple)
40. [All Beauty] Too Faced Chocolate Bar Eyeshadow Palette 16 Shimmer and Matte Shades
41. [All Beauty] ULTA Legendary Lengths Mascara Black/Brown
42. [All Beauty] Ulta Beauty Brilliant Color Eyeshadow ~ Mink
43. [All Beauty] Woochie Water Activated 4-Color Make Up Palette Kits - Professional Quality Halloween Costume Cosmetics - Clown
44. [All Beauty] Youngblood Weekender Palette Value Set | 9 Eyeshadow, 2 Blush, 2 Highlighter | Cruelty Free, Paraben Free, Gluten Free
45. [All Beauty] Youniverse Color-Change Lip Balm
46. [All Beauty] Zuri Naturally Sheer Wet To Dry Pressed Powder - African Sunrise
47. [All Beauty] [CHICA Y CHICO] One shot eye palette series, mat, shimmer, glitter, vivid pigmentation, soft texture, long lasting, 9g (daybrown)
48. [All Beauty] [rom&nd] See-through Matte Tint 6 colors | Long-lasting, Lightweight, Watery at the first, soft matte finish at the last | Lip Tint for Daily Use, K-beauty | 3.8g/0.13oz No.01 PINK FOLD
49. [All Beauty] b.tan magic purple potion gradual glow dark mousse 6.7 fl oz / 200mL
50. [All Beauty] tarte MANEATER double duty beauty liquid liner .017 fl oz SAMPLE SIZE

Return JSON only with this schema:
{
  "cluster_id": 16,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 17

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 17
Cluster size: 583

Representative product titles:
1. [All Beauty] (2 PACK) Vaseline Body Lotion, Intensive Rescue, Soothing Moisture, 20.3 oz
2. [All Beauty] 2Pcs Body Cream，Underarm Cream for Dark Spot Corrector and Remover for Knees, Elbows, Sensitive, Nourishes, Brighten Cream for Armpit2Fl Oz/pcs
3. [All Beauty] Applied Nutrition Anti-Aging Dietary Supplement - 90 Softgels
4. [All Beauty] Auctiv Organic and Natural Sunscreen Lotion with SPF 30
5. [All Beauty] BE IN A GOOD MOOD Body Lotion 400-ml | For Home & Travel Use | Skin Care for Men & Women (PEACEFUL FRESH GREEN)
6. [All Beauty] BTZ Beyond The Zone No Limits Smoothing & Finishing Creme
7. [All Beauty] Bath & Body Works Pleasures Chocolate Amber Body Cream 8 oz
8. [All Beauty] Classica Erotica Rash Free Coochy Shave Cream- 16 oz- Fragrance Free
9. [All Beauty] Designer Skin DS20 Limited Edition, 20th Birthday Bronzer - 13.5 ounces Indoor Tanning Bed Lotion
10. [All Beauty] Ed Hardy ONCE UPON A TAN Hypoallergenic Softening Ultra Dark Tanning Lotion - 10 oz.
11. [All Beauty] Fiesta Sun COCONUT DREAM Moisturizing 16 oz Lotion Extend After Tanning Tan Bed
12. [All Beauty] Gio Naturals Certified Organic Cold Pressed Tamanu Oil - Best Natural Treatment for Dry Skin, Eczema, Acne, Scars, and Psoriasis, 4 Oz
13. [All Beauty] Glossier Milky Oil 3.4 fl oz / 100 ml
14. [All Beauty] Grace Cole White Nectarine & Pear Hand & Nail Cream 2 x 30ml
15. [All Beauty] HerSolution Gel
16. [All Beauty] Hip Lift Up Butt Firming Enlargement Cellulite Removal Cream Fast Results 120g
17. [All Beauty] Honeybee Gardens Totally Natural Watermelon Mist Tinted Lip Balm | Organic, Vegan, Gluten-Free | For a Kiss of Color & Nourishment
18. [All Beauty] Ice Watermelon (Ice Watermelon 24 mg, 30 ml Bottle)
19. [All Beauty] JJlivingYOUTH Essential Oil Based Moisturizer
20. [All Beauty] JOAN RIVERS The Right To Bare Legs 6-Ounce Moisturizer (3-Pack)
21. [All Beauty] Jojoba Natural Body Oil
22. [All Beauty] Kim Jeong Moon Aloe Intensive 2X Cream 1.76 oz + 0.12 oz x 4ea + Signature 3X Cream 1.69 fl.oz CURE+ Moisturizing Set
23. [All Beauty] Le Tan Express Tan Mousse 110ml
24. [All Beauty] Leti At-4 Body Cream 200ml
25. [All Beauty] Mountain Ocean Skin Trip Lip Balm – Three 0.165 Ounce Tubes
26. [All Beauty] NEW Extremely Dry Skin Rescue Body Lotion Healing Moisture Lotion 13.5 FL OZ (400ml) - 1-PACK
27. [All Beauty] No-Crack Night Use Hand Cream 4oz
28. [All Beauty] Nourishing Lip Balm 0.5 oz by Diptyque
29. [All Beauty] Ocean Potion 100% Pure Aloe Gel 20.50 oz (Pack of 5)
30. [All Beauty] Ors Jojoba Oil 5.5 Ounce (162ml) (6 Pack)
31. [All Beauty] Pack of 2 - Hamdard Roghan Badam Shirin (Sweet Almond Oil) - 50ml
32. [All Beauty] Planet Botanicals Body Cream, Cocoa Butter, 3 Ounce
33. [All Beauty] Pure 31 Organic Aloe Vera Oil Infused in Organic Soybean Carrier, 2 fl oz, Perfect For Anti-Hair Loss Treatment, Hydrating & Soothing facial skin
34. [All Beauty] RE:P. CELL CALMING CICA TONIC 10.56 oz / 300ml
35. [All Beauty] Red Rinju Cocoa Butter Lotion 16 oz.
36. [All Beauty] SPF 15 Organic Coconut Oil 200 ml by COCOOIL
37. [All Beauty] Santa Maria Novella Acqua di Colonia - Melograno 3.3oz
38. [All Beauty] Scruples Enforce Sculpting Glaze Extra Firm 1000 ml / 33.8 oz
39. [All Beauty] Shimmering Body Lotion by eSalon - Touch and Glow
40. [All Beauty] Silicea Gastro Intestinal Direct Sachets - Pack of 30 Sachets by Hubner Silicea
41. [All Beauty] Skin so Soft Aqua Express Body Milk Spray 8.4 fl oz
42. [Premium Beauty] Suavecito X Johnny Cupcakes Orange & Cream Pomade Set
43. [All Beauty] Thymes Petite Hand Cream - 1 Fl Oz - Vetiver Rosewood
44. [All Beauty] VELY VELY Artemisia Balance Cleansing Water - Aromatic Herb, Natural Hydration, Anti-Aging, Brightening Glow, Paraben-Free (300 ml/10.14 fl oz)
45. [All Beauty] Vanilla Bean Noel Hand Cream 1 fl oz. 2019
46. [All Beauty] WR Medical Therabath Hydrating Cream - Scentfree, 8 OZ # 0210
47. [All Beauty] Yves Rocher Nutritive Vegetal 24 HR Nourishing Cream 1.6 fl. oz. 50 ml
48. [All Beauty] Zest Fruitboost Citrus Sp Size 10z Zest Fruitboost Citrus Splash 10z
49. [All Beauty] [ PACK OF 1 ] MURRAYS PRO COMB CREAM MOISTURIZER 4 OUNCE EA
50. [All Beauty] eos Smooth Lip Balm Sphere, Sweet Mint 0.25 oz (Pack of 10)

Return JSON only with this schema:
{
  "cluster_id": 17,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 18

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 18
Cluster size: 213

Representative product titles:
1. [All Beauty] 10 Sheets Metallic Temporary Tattoos for Women Body Makeup,150+ Designs Flash Temp Glitter Tattoo, Gold Silver Fake Shimmer Jewelry Tattoos, Elephants, Butterfly, Bracelets Henna for Face Body Paints
2. [All Beauty] 12 Colors Nail Glitter Sequins Maple Leaf Nail Art Sticker Holographic Flakes Diy Nail Decorations Decals for Thanksgiving Nail Confetti Decoration Supplies Manicure
3. [All Beauty] 12 Pack Bollywood Head Bindi Tattoo Nail Bling Art Rhinestone Stick On Reusable
4. [All Beauty] 12sheets Nail Art Snowflake Design Sticker Different Snowflake Christmas Series Mixed Sticker Sheets 10101
5. [All Beauty] 20 Rolls Red Lips Nail Stickers Nail Foil Transfer Stickers Summer Romantic Rose Flamingo Heart Pattern Nail Art Decals and Adhesive Gel for DIY Nail Art
6. [All Beauty] 24 Sheets Full Nail Art Stickers Spring Leaf Flowers Designs Water Transfer Watermark Stickers Flamingo Nail Decals Thanksgiving Nail Wrap Manicure Stickers for Women Girls DIY Fingernail Decorations
7. [All Beauty] 36 Sheets French Stripes Nail Art Stickers Geometric Nail Decals Abstract Colorful Wave Line Irregular Curves Water Transfer Nail Art Supplies DIY for Women Girls (Stripes)
8. [All Beauty] 3D Flower Nail Art Stickers Decals Nail Art Supplies Daisy Sunflower Sakura Rose Flower Wood Pulp Chips Design Nail Decals Sequin for Nail Art Decorations for Acrylic Nails Manicure Decor 4 Boxes
9. [All Beauty] 5 x Daddy's Card - Princess, Yes Daddy, Property of Daddy - Temporary Fetish Daddy Girl Tattoo Set (5)
10. [All Beauty] 8 Sheets Cute Temporary Tattoos for Kids, Spidey and His Amazing Friends Theme Fake Tattoos Stickers, Birthday Party Supplies Party Favors Cute Fake Tattoos Stickers Cartoon Party Decorations for Kids Boys Girls Party Gifts Birthday Decorations Rewards Gifts
11. [All Beauty] Autdor Tattoo Needle Cartridges - 20Pcs Professional Disposable Tattoo Cartridge Needles #10 Bugpin 7 Round Liner (7RL) for Tattooing, Tattoo Cartridge Machine Pen, Tattoo Supplies (1007RL)
12. [All Beauty] Autumn Fall Leaves #5 Nail Art Decals
13. [All Beauty] BEIGUO 22 Pack Christmas Light Necklace and Christmas Glow in the Dark Temporary Tattoo Stickers Party Favors for Kids Boys Girls Toddlers Christmas Stocking Stuffers
14. [All Beauty] Ben Nye Tattoo Cover (NT-1)
15. [All Beauty] Bluezoo (Pack of 8 sheets) Flash Henna Temporary Tattoos Sticker -Brown Color,Mixed More than 50 Different Patterns,Buddha,Necklace,Bracelet for Girls
16. [All Beauty] COKTAK 12Pieces/Lot Black Mountain Temporary Tattoos For Men Boys Women Triangle Marine Sea Wave Body Art Arm Legs Water Transfer Fake Tattoo Forest Sticker Children Tatoos Adult
17. [All Beauty] Cincoworld King Horse Temporary Body Tattoos for Kids, Children, Men, Women, Boys and Girls (Beautiful Pious Religious Crosses and Little Pentagons, Modern Art, Upper Arm, Chest, Leg, Back Tattoo)
18. [All Beauty] Crowley Snake Temporary Tattoo (Set of 2)
19. [All Beauty] GAME OF THRONES VARIETY SET - Flash Tattoos set of 25 assorted premium waterproof metallic jewelry temporary foil party tattoos, metallic tattoo, temporary tattoo
20. [All Beauty] Gold Cheetah Print Temporary Tattoos (5 pack) | Skin Safe | MADE IN THE USA| Removable
21. [All Beauty] Halloween Nail Art Foils Fall Nail Foil Transfer Stickers, 10Rolls Holographic Nail Foil Decals Nails Art Supplies Halloween Pumpkin Skull Spider Web Ghost Design Sticker for Manicure Tips Decorations
22. [All Beauty] JXULE 4 Styles Temporary Instant Tattoo Transfer Eyeshadow Eyeliner Eyes Sticker ( 10 Sheets )
23. [All Beauty] LIDELE Temporary Tattoos Flower butterfly Fake Tattoo non-permanent tattoos Pack of 30 Sheets (D)
24. [All Beauty] Latest hot selling and fashionable tattoo sticker product dimension 6.69x3.74 different beautiful butterflies Golden gold realistic temporary tattoo stickers by InterRookie
25. [All Beauty] Metallic Temporary Tattoos - 12 Sheets Waterproof Gold Sliver Glitter Body Face Tattoo for Women Teen Girls, Over 200 Flash Fake Festival Jewelry Bling Body Art Tat Stickers
26. [All Beauty] NAIL ANGEL 12pcs Nails Strips Nail Art Wrap Nail Art Full Cover Sticker Leopard Prints Sticker Fashion Designs for Women (10153)
27. [All Beauty] NAIL ANGEL 16 Sheets Nail Art Water Decals Water Transfer Sticker Different Painting Pattern Decals for fingernail and toenail Manicure (16sheets) 10080
28. [All Beauty] Nailart NAIL TATTOO STICKER - Halloween - cat - black
29. [All Beauty] Nailart NAIL TATTOO STICKER - music / notes / saxophone - black
30. [All Beauty] Oottati Small Cute Temporary Tattoo Red Lotus Lotus Shoulders (Set of 2)
31. [All Beauty] PUISUIT Tattoo Aftercare Waterproof Bandage,Transparent Hygienic Adhesive Wrap Protect and Heal Tattoo 6 inch x 5.5 yd Roll,Second Skin Protective Tattoo Film (Include Glasses-Shaped Folding Scissors)
32. [All Beauty] Pack of 4200 3/4" Round Color Coding Circle Dot Labels, 10 Bright Neon Colors, 8 1/2" x 11" Sheet, Fits Any Printer
33. [All Beauty] S8 Red Tattoo Stencil Paper 100-Sheets (Hand or Machine USE)
34. [All Beauty] SHENGHUO Halloween Sleeve Temporary Tattoos 6-Sheet, Death Skull Tatoos Black Body Tattoo Stickers for Adults, Men, Women, Girls, Kids, Halloween Parties Makeup
35. [All Beauty] SanerLian Set of 5 Waterproof Temporary Fake Tattoo Stickers Watercolor Grey Crow Birds Swallow
36. [All Beauty] Semi permanent plant temporary tattoo stickers, lines / flowers / stars / Floral butterfly dark temporary tattoo stickers, suitable for adults, girls and boys, lasting 1-2 weeks, natural fading (E)
37. [All Beauty] Small Tattoos Black Realistic Temporary Tattoos for Women Men Adults Waterproof Tiny Fake Tattoos Body Stickers Word Cross Anchor Flower Temp Tattoo Paper Finger Neck Wrist Ankle Tattoo (40 Sheets)
38. [All Beauty] TAFLY Temporary Tattoos for Women Blue Butterfly and Black Rose Arm/Leg/Body Art Transfer Tattoos 5 Sheets
39. [All Beauty] TOODOO 8 Sets Mermaid Face Gems Glitter Sticker Rhinestone Bindis Crystal Face Jewels Tattoo Forehead Decorations for Women Favors (Pattern Set 4)
40. [All Beauty] Tattify Dragonfly Temporary Tattoo - Keep Flying (Set of 2)
41. [All Beauty] Tattify Various Infininty Sign Temporary Tattoos - Everlasting Life (Complete Set of 12 Tattoos - 2 of each Style) - Individual Styles Available - Fashionable Temporary Tattoos
42. [All Beauty] Tattoo Concealer, Skin Scar Concealer Cream for Tattoo Cover Up, Vitiligo Spots Birthmarks Hiding, Makeup Set for Age Spots & Cover Bruises with Waterproof Design
43. [All Beauty] Temporary Tattoo Factory Stripteaze Naughty Tattoos - Naughty Ultra Realistic Fake Adult Temporary Tattoos a little Trashy and Slutty Words Tattoos for Women's Hip, Lower Back, Thigh, Arm Tramp Stamp - Long Lasting (30Pack)
44. [All Beauty] Tribal Totem Temporary Tattoo for Men 8 -Sheets Fake Black tattoo Body Stickers Arm Shoulder Chest (style1)
45. [All Beauty] Unicorn Party Supplies Tattoos for Kids - 36 Glitter Styles | Unicorn Party Favors and Birthday Decorations
46. [All Beauty] WOKOTO 6Pcs Cute Nail Art Design Polish Stickers Wraps Self Adhesive Bow Tie Leopard Print Design Manicure Stickers Decals Set with 1Pc Nail Buffers Files
47. [All Beauty] WYUEN 5 Sheets New Design Temporary Tattoo Mountain Waterproof Tattoo Sticker For Women Men Body Art 9.8X6cm FE-043
48. [All Beauty] Women Beautiful Flower Pattern Nail Art Decoration Stickers Floral Nail Decals for 1 Sheet (3)
49. [All Beauty] black face jewels for make up face gems stick on festival body gems black face Rhinestone Diamond halloween mermaid tattoo Stickers
50. [All Beauty] rainbow tattoo-Meteor shower-45pcs

Return JSON only with this schema:
{
  "cluster_id": 18,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

## Cluster 19

```text
I clustered ecommerce products using KMeans on title-only Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 19
Cluster size: 330

Representative product titles:
1. [All Beauty] 2 Pack Detangling Brush for Curly Hair, Wiisdatek Black Hair Detangler, Afro Textured 3a to 4c Kinky Wavy, Detangle Easily Wet/Dry/Long Hair for Beautiful Shiny Curls (Pink, Green)
2. [All Beauty] 2 Pcs Detangler Brush,Detangler Hair Comb or Brush for Adults and Kids Hair Comb
3. [All Beauty] 21°C 4 Pieces Detangling Brush and Hair Comb Set Knots Detangler Easy to Clean for Kinky Wavy Curly Coily Wet Dry Oil Thick Long Natural Hair(Pink)
4. [All Beauty] 2Pack Detangling Brush for Curly Hair, Green Hair Detangler, Afro Textured 3a to 4c Kinky Wavy, for Wet/Dry/Long Thick Curly Hair, Exfoliating Your Scalp for Beautiful and Shiny Curls
5. [All Beauty] 800pcs Elastic Rubber Hair Bands, WSYUB Hair Tools with Rattail comb, Gentle Edges Brush,Topsy Tail Tools
6. [All Beauty] ANNIE Jumbo Detangler Comb (Model:121)
7. [All Beauty] Afro Twist Hair Comb-Barber Favored,2 in 1 DIY Men's Curly Hair Style African Style Hair Brush (Red)
8. [All Beauty] Baby Hair Clippers - Electric Hair Trimmer with 3 Heads & 3 Guide Combs, Quiet & Professional, Rechargeable Waterproof Cordless Haircut Kit for Kids Infants Men and Women (Mint)
9. [All Beauty] Barber Cape and Neck Duster Brush Comb Set, Waterproof Hair Cutting Cape Professional Hairdresser Cape Salon Supplies Tool Set for Hair Treatment/Cutting/Coloring/Perming(55x63Inch)
10. [All Beauty] Beard Brush & Comb Kit for Men – With Wild Boar Bristles for Easy Grooming. Use With Beard Conditioner or Softener to Get Perfect Facial Hair & Moustache Growth.
11. [All Beauty] Beard Starter Oil and Comb Set For Men, Elegant Bearded Starter Kit Includes Beard Moisturizer Oil 15ml, Silver Metal Comb, Birthday, Anniversary, Christmas Beard Kit for Men Gift
12. [All Beauty] Big Red Beard Combs - Handcrafted No. 16 Hardwood Blade Beard Comb (Available in Cherry or Walnut) (Walnut)
13. [All Beauty] Comb Resin Molds, Hair Pick Silicone Molds Female Resin Mold 3 Pieces Epoxy Casting Comb Molds, Modeling Tools DIY Hairdressing Styling Tools
14. [All Beauty] DELE Pet Dog Cat Grooming Tools Kit 5 in 1 Box Set, Pin Comb, Nail Clipper, Slicker Brush, Dematting Comb with 3M Retractable Dog Leash for Medium/Small Pet Dogs Puppies Cats Gift (Blue)
15. [All Beauty] DOMAVER Beard Straightener Brush, Cordless Beard straightening Comb, Portable USB Rechargeable LCD Display Beard Brush Anti Scald Electric Heated Beard & Hair Ionic Straightener Brush for Men & Women
16. [All Beauty] Denman D-100 Large Tunnel Vent Hair Brush
17. [All Beauty] Denman D31 7-Row Medium Volumizing Brush (Pack of 2)
18. [All Beauty] Detangling Brush for Black Natural Hair,Hair Detangler Brush for African American 3a/4b/4c Kinky Wavy,Curly,Coily,Thick Hair, Wet n Dry,Improve Hair Texture-Easy Clean (Green with Small Handle)
19. [All Beauty] DigHealth 12 Pcs Hair Cutting Scissors Kit, Professional Hairdressing Scissors Kit with Stainless Steel Thinning Scissors, Comb, Cape and Clips, Hair Cutting Shears Set for Baber, Salon and Home
20. [All Beauty] GNAWRISHING Flea Comb 6Pcs with High Strength Teeth Durable Pet Tear Stain Remover Combs, Pet Dog Cat Grooming Comb Set Effective Float Hair Remover…
21. [All Beauty] GSGO Bamboo Hair Brush Natural Detangler with Carry Bag For All Hair Types,Improve Hair Growth, Bamboo Pin Bristles Massage Scalp For Healthy Shiny Hair.
22. [All Beauty] Generic SYEB Self Cleaning Slicker Brush for Dogs and Cats, Pet Grooming Shedding Brush with Quick Release Button, Massages Particle & Promote Circulation (Blue)
23. [All Beauty] HENMI Makeup Brush Cleaner, 2 Speeds Best Electric Cleaning Tool USB Automatic Brush Cleaner & Dryer with 8 Rubber Collars for Size Brushes, Cosmetic Brush Spinner for Beauty Lovers
24. [All Beauty] HICC GROOM! Pet Hair Remover, Self-Cleaning Pet Grooming Roller, Reusable Dog & Cat Fur Removal Tool for Furniture, Couch, Carpet, Bedding, Car Seat
25. [All Beauty] HYOUJIN 3pcs Salon Hair Coloring Dyeing Kit,Large Tint Brush,Color Mixing Tint Brush Combs,Dye Brush,Bleach Tint,Dye Brush Set,Hair Coloring Kit,Dye Brush Set,Color Applicator (Multicolor)
26. [All Beauty] Hair Cutting Combs Barber Hair Comb Carbon Fiber Pet Comb Heat Resistant Cutting Comb Long Hair Comb Styling Comb Size Marked Doubtless Bay (3pcs)
27. [All Beauty] Hair Cutting Umbrella Easy to make haircut at home! for every person for all age group from child to elder: A Barber Cape at home
28. [All Beauty] Hair Massager Brush Electric Fast Hair Straightener LCD Ion Anti-Scald Comb (Pink)
29. [All Beauty] Hair Shampoo Brush & Body Brush 2-in-1 Kit, ALLYAG Soft Silicone Hair Scalp Massager and Body Scrubber for Exfoliate and Improve Blood Circulation, Used in Wet & Dry, Fit for Women, Men, Kids, Pets
30. [All Beauty] Leegoal 4 Pieces Professional Fiber Hair Cosmetic Makeup Brush Set with Beige Case
31. [All Beauty] LucaSng Tangle Comb 3A to 4C Tangle Brush for Curled Wavy/Curly/Wet/Dry/Oily/Thick/Long Hair, Knotted and Tangled are Easy to Clean
32. [All Beauty] L’ange Hair SIENA Thermal Hair Brush - 33mm Round Barrel Hair Volumizer Brush with Nylon Bristles for Women, Men & Kids - Professional Non Slip Hair Styling Brush for All Hair Types - MSRP $32.00
33. [All Beauty] Medium Tooth Comb Red Sandalwood Handle and Buffalo Horn Teeth Handmade Comb - JM008
34. [All Beauty] Molain Cat Dog Flea Comb, Pet Tear Stain Remover Comb Set Pet Dog Cat Grooming Comb (5 Pieces)
35. [All Beauty] Nollary Pet Brush for Shedding Grooming Undercoat Massage Self Cleaning Slicker Brush for Long Short Haired Dogs Cats Bunny Rabbits Lambs
36. [All Beauty] Pet Grooming Tool Flea Removal Comb Zinc Alloy Tightly Spaced Teeth,Professional Anti-Static Dog, Cat, and Pet Rotating Pin Comb, Best for Removing Knots and Mats
37. [All Beauty] Sanbi - R 352 Hairbrush
38. [All Beauty] Scalpmaster Teasing Brush/Comb
39. [All Beauty] The EZ Detangler Hair Brush, Detangling Brush, Detangling Hair Brush, Hair Brush for Natural Hair-Detangler (Black)
40. [All Beauty] Tinksky 2pcs Stainless Salon Barber Hair Cutting Thinning Scissors Shears Hairdressing Set
41. [All Beauty] Titania Copper Round Styling Hair Brush - Premium Styling & Hairblowing Hairbrush w/Black Satin Handle & Nylon Pins - Improves Straight, Curly & Fine Natural Hair, Extensions & Wigs
42. [All Beauty] Waterproof Barber Cape Protector Haircut Cloth Apron Neck Duster Brush Barber Supplies Tool Set
43. [All Beauty] WavEnforcer Boar Bristle Pocket-Size Military Crown Brush Beard Brush ✮ Best Brush for Hair, Waves, Travel, Pocket ✮ Medium Firmness
44. [All Beauty] Wet brush, Detangling brush and shampoo brush 3 pcs, soft and firm, suitable for all hair types of men and women, can be tangled and tangled easily.-red
45. [All Beauty] Wood Beard Combs for Men-Mustache Grooming-pocket beard comb-Natural Neem Wood-Antistatic,Snag free,wide tooth-Perfect with Beard Balms and Beard oils
46. [All Beauty] Yellow Sunflwer Nylon Hair Brush For Wet/Dry Hair Smoothing Massaging Detangling, Air Cushion Comb For Women Men Kid, Detangler For All Hair Types
47. [All Beauty] ZRKFSR Pet Grooming Tool，2 Sided Undercoat Rake for Dogs &Cats，Deshedding Tool Great for Short to Long Hair Cats &Large Small Dogs，Safe and Effective Dematting Comb for Mats &Tangles Removing (Blue)
48. [All Beauty] Zou.Rena Little Girls Hair Brush Easily Brushed Through Tangles-No Liquid,Glitter Confetti Combs Gifts Play for Kids Age 3-8 (Fox)
49. [All Beauty] upain 16Pcs Rat Tail Comb Fiber Pintail Hair Combs Professional Styling Combs Heat Resistant with Stainless Steel Pintail for Women Girls Hair Styling, 4 Colors
50. [All Beauty] uxcell 2 Pcs Travel Lady Black Fine Teeth Foldable Dual Pocket Straight Hair Comb

Return JSON only with this schema:
{
  "cluster_id": 19,
  "label": "short taxonomy label, 2-6 words",
  "parent_label": "broader parent category, 1-4 words",
  "description": "one sentence describing what belongs in this cluster",
  "confidence": "high | medium | low",
  "include_keywords": ["keywords or product types that belong here"],
  "exclude_keywords": ["nearby but different product types to avoid"]
}

Guidelines:
- Prefer labels a shopper or merchandiser would understand.
- Use the product titles as evidence; do not overfit to one unusual sample.
- If the cluster mixes multiple themes, choose the dominant theme and set confidence to medium or low.
- Keep labels distinct from other likely ecommerce taxonomy labels.
- Do not include markdown or commentary outside the JSON.
```

