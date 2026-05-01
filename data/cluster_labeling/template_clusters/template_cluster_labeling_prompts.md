# Template Cluster Labeling Prompts

## System Prompt

You are an ecommerce taxonomy expert.
Your task is to label product clusters using representative product titles.
Return concise, shopper-friendly taxonomy labels.

## Cluster 0

```text
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 0
Cluster size: 403

Representative product titles:
1. [All Beauty] (6 Pack) NYC Waterproof Eyeliner Pencil - Black
2. [All Beauty] 1+1 Mascara Applicator Guide Tool Mascara Shield Eyeliner Guide Template Eye Makeup Tool
3. [All Beauty] 12pcs Zhalya Full Makeup Brushes Set with Large Size Foundation Brush, Blending Face Powder, Blusher, Concealer, Eyeliner, Eyeshadow Brush, Comes with PU Leather Bag for Storage.
4. [All Beauty] ANNATATO BEAUTY Eyebrow Pen, Upgrade Eyebrow Pencil with a Micro-Fork Tip Creates Natural Eyebrow Makeup (Chestnut)
5. [All Beauty] Avon True Color Glimmersticks Eye Liner Set 4 Pcs. Blackest Black, Starry Night Blue, Smoky Diamond, and Sugar Plum
6. [All Beauty] BallHull 300 Pcs Mascara Wands Applicator Disposable Eyelash Makeup Brush for Eyelash Extension Eyebrow and Brow Definer, Black
7. [All Beauty] Biange Professional 10 Pieces Makeup Brush Set, 5 Essential Shapes, Soft Synthetic Fiber, Foundation Blending Blush Face Powder Eyeshadow Cosmetics Beauty Brush, Makeup Brush Kit Tools (Gold Black)
8. [All Beauty] Blue Eyes Lashes Mascara Applicator / Application Guiding Tool With Eyelashes Comb And Pink Silicone Blackheads Facial Pores Cleaner / Face Skin Cleanser By VAGA
9. [All Beauty] CCbeauty 6-Packs Double Ended Spoolie and Angled Eyebrow Brushes Set Makup Eyebrow Kit and Eyebrow Comb for Application of Brow Powders Waxes Gels and Blends (#3)
10. [All Beauty] Ciyee 2016 New 90 degrees bending rose gold Oval brush set 10pcs Powder Blusher Toothbrush Curve Cosmetic makeup brush set ,lipstick /foundation/eyeliner /blush/concealer / Linear Brush (Gold)
11. [All Beauty] DIAREGNO Teeth Whitening Pen (2 Pens) - 20+ Uses, Effective ＆ Painless, No Sensitivity - Beautiful White Smile - Natural Mint Flavor
12. [All Beauty] DIOLAN 15 PCs Makeup Brushes Set for Foundation Blending Blush Eyeliner Face Eye Shadow with Synthetic Fiber Bristles & Wooden Handles, Includes Wine Red Travel Bag
13. [All Beauty] Eglips Eye SHADOW STICK Waterproof Soft Texture Twist-Up Dramatic Look (Beech)
14. [All Beauty] EyeBlack Pink Grease Stick
15. [All Beauty] Eyebrow Stamp and Stencil Kit, One Step Eyebrow Stamp Shaping Kit with Eyebrow Slant Tweezer, Long Lasting Waterproof Brow Powder 24 Styles Reusable Stencils with 3 Brushes Professional Makeup Tool (Black)
16. [All Beauty] Eyebrow Tattoo Pencil with Eyeliner Pen, Eyebrow Pencil Eye Makeup Long Lasting Waterproof & Smudgeproof 3 Style (Chestnut)
17. [All Beauty] FINEJO Women's Makeup Cosmetics Tools Set 15 Colors Creamy Concealer Kit and 1 Brush
18. [All Beauty] Farmasi Make up Exspress Waterproof Eye Pencil, 1 g. (Blue)
19. [All Beauty] Flowfushi UZU Eye Opening Liner Liquid Eyeliner (Purple)
20. [All Beauty] Hair Chalk - 10 Pcs Temporary Hair Chalk Comb Hair Dye For Halloween Celebration Make Up Party Cosplay And Diy Non-toxic And Easily Washable Adults (hair chalk 10PCS)
21. [All Beauty] Heidi 32pcs Makeup Brushes Travel Set Professional Foundation Powder Cream Blush Cosmetic Brush Kits with Leather Bag Case Pink
22. [All Beauty] JAF Large Kabuki Bronzer Brush for Loose & Pressed Powder Mineral Foundation, Portable Face Makeup Bronzing Blush Highlighter Brush in Traveling (18SW-B） Big Fluffy Setting & Finishing Powder Brush
23. [All Beauty] JSDOIN Makeup Brushes Makeup 14 PCs Makeup Brush Set Premium Synthetic Kabuki Foundation Face Powder Blush Eyeshadow Brushes, Rose Golden
24. [All Beauty] Jordana Cat Eye Liner 03 Orchid
25. [All Beauty] KGEND 1PC Pro Nail Art Dust Cleaner Face Blush Brush ,Cosmetic Gift (Pink)
26. [All Beauty] KYDA 3 Pcs Eyebrow Pencil Set, 2 in 1 Eyebrow Pen, Double-end Eyebrow Pencil with Brush and Eyebrow Powder, Waterproof&Longlasting Natural 3D Eyebrow Makeup-Gray
27. [All Beauty] La Fresh Travel Lite (10) Make-Up Remover Wipes Individually Packaged, Large Size. Plus Bonus Velvet Eyeliner Pen
28. [All Beauty] M.A.C Pro Longwear Waterproof Brow Set Bold Brunette
29. [All Beauty] Make up Brushes, VANDER LIFE 32pcs Premium Cosmetic Makeup Brush Set for Foundation Blending Blush Concealer Eye Shadow, Cruelty-Free Synthetic Fiber Bristles, Travel Makeup bag Included, Black
30. [All Beauty] Makeup Brush Set 6 Pcs For Premium Synthetic Kabuki Foundation Face Powder Blush Eyeshadow Brushes Makeup Brush Kit with Blender Sponge and Brush Cleaner (white)
31. [All Beauty] Marine Forest Eyebrow Stamp Stencil Kit, One Step Brow Makeup Eyebrow Stamp and Shaping Kit for Perfect Brows, Waterproof and Long Lasting (Dark Brown)
32. [All Beauty] Maybelline New York Colossal Bold Eyeliner, Black, 3g
33. [All Beauty] Newfacefure Magnetic Eyeliner, High-end Formula Magnetic Liquid Eye Liner Pen, Waterproof and No Smudge with Natural Look Eye Makeup Liner, Use with Magnets Lashes (Brown)
34. [All Beauty] ONLY 1 IN PACK Maybelline Color Blur Cream Matte Pencil + Smudger, 50 I Like to Mauve It
35. [All Beauty] One Step Eyebrow Stamp Shaping Kit Brow Powder Stamp with 12 Reusable Eyebrow Stencils with Eyebrow Pen Brushes, Long Lasting Waterproof Buildable (Light Brown)
36. [All Beauty] PONY EFFECT Inkfit Brush Liner | #Carbon Black | Brush Eyeliner, Smudge-proof, Long-lasting | K-beauty
37. [Premium Beauty] Physicians Formula Eye Booster Feather Brow Fiber & Highlighter Duo, Black/Brown, 0.04 Ounce
38. [All Beauty] QMSILR 16PCS Eyeshadow Applicators Disposable Eyeshadow Brushes Small Eye Shadow Sponge Applicator Set Tipped Eye Makeup Tool (Pink, Green)
39. [All Beauty] SACE LADY Waterproof Tinted Bow Gel, Long Lasting Sculpting Mascara Eyebrow Pomade Cream Color for Eyebrow Makeup, Flake-proof, Smudge-proof, Non-clumping (Blonde)
40. [All Beauty] SECRET KEY Self Brow Tattoo Tint Pack 8g / Beautynet Korea (#2 Mocha Brown)
41. [All Beauty] SUNTON 12 Color Temporary Hair Chalk Pens, Washable Hair Color Dye Face Kit Safe for Makeup Birthday Party Gift for Girls Kids Teen
42. [All Beauty] Sonia Kashuk Twist Up Longwear Eye Liner Pencil (Black Diamond 02)
43. [All Beauty] Swan makeup brush set 11pcs eye shadow brush concealer professional makeup brush
44. [All Beauty] Syntus Makeup Brush Set, 11 Makeup Brushes & 4 Blender Sponges & 1 Brush Cleaner Premium Synthetic Foundation Powder Kabuki Blush Concealer Eye Shadow Makeup Brush Kit, Pink Golden
45. [All Beauty] Tanali Glitter Shimmer Highlighter Eyeshadow Palette with 6pcs Eye Shadow Makeup Brushes Set (#2)
46. [All Beauty] VANDER Makeup Brushes 24 Pieces Professional Makeup Brush Set Synthetic Kabuki Foundation Blending Blush Face Eyeliner Shadow Power Brushes Liquid Cream Concealer Lip Cosmetics Brushes Kit (Wood)
47. [All Beauty] Woman Makeup Eyebrow Stamp Kit Waterproof Eyebrow Stamp and Shaping Kit Eyebrow Definer for Women Eyebrow Makeup Gift for Women Girl (with 24Eyebrow Stencils,Dark brown)
48. [All Beauty] World Traveler Black and White Peace Sign Makeup Brush Bag 10-inch
49. [All Beauty] XICHEN Long Lasting Waterproof Stick Two-color eye shadow pen, eye shadow stick Shimmer Eyeshadow Cream (Mysterious purple)
50. [All Beauty] Yves Saint Laurent YSL The Shock Volumizing Mascara 01 Asphalt Black, 0.06 oz Mini

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 1
Cluster size: 528

Representative product titles:
1. [All Beauty] 10PC Babys Headband Hairband, Misaky Elastic Wave Point Bowknot
2. [All Beauty] 12pcs Baby Girls Turban Knotted Headband Elastic Bows Hair Band for Infants Toddler Newborn
3. [All Beauty] 3 Pieces Shower Cap for Women, Triple Layers Extra Large Bath Caps with Dry Hair Waterproof Shower Hair Bath Cap Reusable Hair Dryer Cap Silky Satin Shower Hat Bonnet (Purple, Green, Pink)
4. [All Beauty] 3 Pieces Soft Sleep Cap – Night Satin Bonnet with Wide Premium Elastic Band for Women
5. [All Beauty] 3 Styles Camouflage Headband Headwrap (Style 3)
6. [All Beauty] 6 Pieces Shower Cap for Women Reusable Hair Shower Cap Waterproof Bowknot Bath Caps Adjustable Bow Bath Caps for Girls Long Hair Shower Bathing Spa Home Travel, 6 Styles
7. [All Beauty] 6pcs Full Cover Fleece Ear Warmers Headband- Fleece Winter Headbands Cold Weather Earmuffs Ear Muffs Cover Headband for Running Skiing Cycling Yoga Outdoor Sports (Black, Pink, Grey)
8. [All Beauty] 8Pack Women's Headbands Yoga Workout Exercise Headband Sweat Wicking Hair Bands (Color M)
9. [All Beauty] 9 Pieces Satin Bonnet Sleep Caps Night Sleeping Head Covers Double Layer Shower Caps Salon Bonnet Hair Covers with Wide Elastic Band for Women Long Curly Straight Hair Braids, 9 Colors
10. [All Beauty] ANBALA Tiara Crowns, Wedding Pageant Crowns Princess Crown Rhinestone Crystal Queen Tiara Headband for Women (Silver)
11. [All Beauty] BABEYOND Vintage 1920s Flapper Headband Roaring 20s Great Gatsby Headpiece with Feather 1920s Flapper Gatsby Hair Accessories
12. [All Beauty] Baby ShowerCap, Bigban Baby Shampoo Shower Bathing Bath Protect Adjust Soft Cap Hat New (Pink)
13. [All Beauty] Bow Hair Band Lovely Rabbit Ears Soft Carol Fleece Bowknot Makeup Cosmetic Shower Elastic Hairlace Headband(pink)
14. [All Beauty] Burgundy 2 Inch Velvet Covered Headband with Teeth Women and Girls wide Hair Band
15. [All Beauty] Button Headband Holder for Nurses Mask, Women/Men/Yoga/Sports, Protect you Ears with Button Headband, Suit for Everyone Wearing
16. [All Beauty] Button Headbands 4 Pack for Women Nurses, Knotted Hair Wraps Holder for Ears,178A
17. [All Beauty] COSYOO Fashion Boho Headbands for Women 12PCS Hair Band Elastic Vintage Button Knotted Headbands Head Wrap Floral Bandeau Headbands
18. [All Beauty] Catery Boho Headbands Vintage Flower Printed Head Wrap Criss Cross Elastic Hairband Fashion Hair Accessories for Women and Girls (Set 7-5 Pack)
19. [All Beauty] FAELBATY 2 Pcs Headbands for Women Knotted Headbands Glitter PU Wide Headbands for Women Cute Hairbands Fashion Knot Headband for Women(Black & Silver)
20. [All Beauty] Gegado Headbands with Buttons for Mask, Nurse Gifts for Women, Nurse Accessories for Work, Nurse headbands Non-Slip Stretchy Moisture Wicking Sweatband Sports Headbands 6pcs
21. [All Beauty] Gifts and Beads |Sky Daisies and mini polka dots,1 Headband, hair bands, gifts for women, headband for girls, wide headband, handmade in USA, wide hair band, flowers printed cotton fabric,wrapped plastic base, fashion headbands and headwrap for women and girls, diademas para mujeres y ninas.
22. [All Beauty] HUIANER Rose Flower Headband Bohemian Style Elastic Hair Band Floral Accessories For Seaside Holiday Festival Wedding, Pack of 6
23. [All Beauty] Headband of Women , 3 Packs Wide Edge Velvet Twist Braided Hair Band , Solid Color Fashion Hair Bands. (Green/Yellow/Rose red)
24. [All Beauty] Headbands For Women Cotton Stretch Headbands Elastic Yoga Hairband for Teens Girls Women Adults, Assorted Colors, 10 Pieces (Black)
25. [All Beauty] Headbands for Women 20 pcs, Boho Floal Style Criss Cross Head Wrap Hair Bands with 1 Storage bag
26. [All Beauty] Headbands for Women Padded Headbands - 1PCS Velvet Headband Elegant Headbands Hairpins Headwear Barrette Styling Tools Accessories for Women and Ladies,Black
27. [All Beauty] Hedume 6 Pack Shower Caps, Waterproof & Adjustable Bath Cap for Women, Double Layered Shower Cap, Oversized Design for All Hair Lengths, Elasticized Hem
28. [All Beauty] Jaciya 10 Pieces Rose Flower Headband Hair Band Flower Crown Floral Garland Headbands for Women
29. [All Beauty] Jeairts Boho Leopard Headbands Criss Cross Hair Bands Twisted Turban Head Wraps Elastic Fabric Head Scarfs Stylish Yoga Hair Accessories for Women and Girls (Leopard White)
30. [All Beauty] Knot Headband for Women Girls,Sun Flower Headbands Wide Headbands Turban Headband Hair Band Bandana Hairband Head Band Wrap with Bow Cloth Wrapped Headwear,Blue
31. [All Beauty] LIHELEI Wide Headband for Women, Thick Knitted Headband Fashion Head Wrap in Solid Color Non-slip for Daily Festival Gift-4PCS Black/Red/Maroon/White
32. [All Beauty] LOVINO Women Headbands Elastic Turban Head Wrap Headband Yoga Headbands Knotted Hair Band Accessories for Fashion Sport 4 Pack I
33. [All Beauty] LifeDawn 4 Pieces Khaki Headband Knotted Headband Wide Headbands for Women Girls, Non Slip Fabric Headbands Elastic Headwear Barrette Styling Tools Accessories
34. [All Beauty] MarchQueen Boho Headbands for Women's Hair Non Slip Knottd Headbands Solid Color Ribbed Stretchy Hair Bands for Women Girls Yoga Headwraps Hair Accessories 6Pcs(Solidcolor1-6pcs)
35. [All Beauty] Ms.Gaga 7PCS Girl Baby Headband Toddler Lace Bow Flower Hair Band Accessories
36. [All Beauty] ONIE 6 Pack Multi Color Reversible Sequin Cat Ears Headband One Size Fits - Kids and Adults for Party, Holiday, Halloween Christmas Casual Wear
37. [All Beauty] Padded Headband Satin Fashion Headbands for Women multi-color Statement Light thick sponge plastic Retro Grace Elegant Wide Plastic Hairbands For Woman
38. [All Beauty] QMSILR Satin Bonnet Sleep Cap Double Layers Silk Bonnet for Women Hair Care Elastic Wide Band Night Hat Head Cover for Natural Long Hair Curly Hair 2 Pack (Black, Beige)
39. [All Beauty] Spa Facial Headband, Ztent Make Up Head Wrap Washable Terry Cloth Headband Adjustable Stretch Towel with Magic Tape For Face Wash Facial Treatment Sport (4 Packs)
40. [All Beauty] Surkat Women Stain Shower Caps Double Layer African Printing Bonnet Cap Bath Hat Rose Pink
41. [All Beauty] Turbie Twist Microfiber Hair Towel Wrap [2 Pack] – The Original Microfiber Hair Wrap As Seen On TV! Signature Prints [Purple] Hair Turban Towel Wraps – Plopping Towel for Long and Curly Hair Women
42. [All Beauty] Unaikoo Shower Cap for Women Reusable Waterproof Silk Satin Bonnet For Women, Double Layer Polyester Shower Cap, Bathing Cap Hair Cap For Shower with Ribbon Bow Green
43. [All Beauty] Unicra Head Chain Jewelry Vintage Hair Accessories Silver Decorative Headbands for Women and Girls (Gold)
44. [All Beauty] Valdler Womens Girls Flower Feather Mesh Net Beaded Fascinator with Headband Tea Party Derby Hat Wedding Hair Accessory Red
45. [All Beauty] WELLVO 20PCS Disposable Medical Bouffant Caps Thickened Non-woven Doctor's Hat for Labs, Nurse, Tattoo, Food Service, Health, Hospital
46. [All Beauty] Wide Band Bonnet Night Sleep Cap Sleeping Head Cover for Women Girls (Black Floral+Light Pink Floral,2 Pieces)
47. [All Beauty] Woeoe Boho Turban Criss Cross Headbands Stylish Wide Red Yoga Head Wraps Knotted Outdoor Elastic Head Scarfs for Women and Man (Pack of 3)
48. [All Beauty] Women Headbands, Elastic Headbands with Buttons, Headbands with Buttons for Women Men , Non Slip Hair Bands for Yoga Sports Running (HHNK08-6pcs)
49. [All Beauty] ZOCONE 10 Packs Boho Headbands for Women Girls, Turban Headwraps for Sports Yoga Running Workout, Elastic Fashion Hair Band (A)
50. [All Beauty] Zucker Feather (TM) - Marabou Antenna Headband w/Lurex Dark Lilac/Opal Lurex

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 2
Cluster size: 466

Representative product titles:
1. [All Beauty] American Crew Forming Cream 1.75 oz (Pack of 4)
2. [All Beauty] Arctic Fox Semi Permanent Hair Color Dye 8 Ounce (Cosmic Sunshine)
3. [All Beauty] As I Am Naturally 8pcs ULTIMATE JUMBO COMBO (Curl Shampoo, Leave-In Conditioner, So Much Moisture, Cocoshea Whip, Cocoshea Spray, Smoothing Gel, Detangling Conditioner and Cocnut CoWash)
4. [All Beauty] Aunt Jackie's Grapeseed Style&Shine Recipes Hair Care (CONDITIONER)
5. [All Beauty] Aussie Moist Shampoo and Conditioner, 13.5 Ounce Each, Plus 3 Minute Miracle Moist, 8 Ounce
6. [All Beauty] Aussie Shampoo 2-N-1 Miracle Moist 12.1 Ounce (360ml) (2 Pack)
7. [All Beauty] Beard Starter Oil and Comb Set For Men, Elegant Bearded Starter Kit Includes Beard Moisturizer Oil 15ml, Silver Metal Comb, Birthday, Anniversary, Christmas Beard Kit for Men Gift
8. [All Beauty] Black Caviar Shampoo & Shower Gel for Men 2 in 1 400ml 13.52fl.oz
9. [All Beauty] Cantu Shea Butter Conditioner Hypoallergenic 8 Ounce (236ml) (2 Pack)
10. [All Beauty] Citre Shine Shine Miracle Extra Strength Anti-Frizz Serum, Highly Laminating 4 fl oz (118 ml)
11. [All Beauty] DESIGNLINE Curl Lock Leave-in Moisturizer, 8 oz - Regis Leave-In Conditioner Treatment that Helps with Shape Retention and Works as an Instant Detangler for Defrizzing Curly Hair (8 oz)
12. [All Beauty] DESIGNLINE Moisture Shampoo, 33.8 oz - Regis Sulfate Free Formula Gently Moisturizes and Cleanses Hair to Keep Hair Color Safe and Healthy (33.8 oz)
13. [All Beauty] Dudley’s Total Control Edges & Ends 4oz
14. [All Beauty] Fitoxil Intensive Anti Hair-loss Treatment 5 X 10ml
15. [All Beauty] Formula of Beauty Korean Shampoo and Conditioner - Damaged, Oily Hair, Daily Scalp Care - Plant Based All Natural Shampoo and Conditioner set Paraben, Sulfate Free - Dream Me Blue (10.5 fl oz /300 ml)
16. [All Beauty] Green Pharmacy. Balm Hair conditioner Linden flower and Sea Buckthorn oil. For dry and damaged hair (Липовый цвет и облепиховое масло)
17. [All Beauty] Gueye Mother Nature's Best Hair Growth-L30
18. [All Beauty] Hair Chalk Comb for Beautiful Salon Hair Highlights. Temporary Hair Color with Applicator. Hair Salon Toy for Green Hair. Paint & Style Hair Care - No Need to Wet Hair. Ready in Minutes.
19. [All Beauty] Infinity 8-in1 Keratin Leave In Hair Treatment 8.5oz
20. [All Beauty] JU POPPIN EDGE CONTROL
21. [All Beauty] Kristin Ess Scalp Detoxifying Bubble Mask, Pre-Shampoo Foaming Scalp Treatment, 4.5 Ounces
22. [All Beauty] La Bella, Hair Gel, Max Hold Styling Gel, Avocado Oil, 22 oz, Pack of 2
23. [All Beauty] Mineral Salt Texture Paste, 2 oz - Regis DESIGNLINE - Ultimate Multi-Tasking Styling Paste with Semi-Matte Finish for Damp, Dry, Long, or Short Hair (2 oz (2 Pack))
24. [All Beauty] Natural Oil Control Fast-Drying Working Hair Spray 10 oz
25. [All Beauty] Nexxus Hair Conditioner Sheer Frizz Resistance, 25 oz (Pack of 2)
26. [All Beauty] Nick Chavez Velvet Mesquite Serum For Hair & Skin 4 oz Double Size
27. [All Beauty] OYIN 8.4 oz. Hair Dew Daily Quenching Hair Lotion and OYIN 8 oz. Whipped Pudding Rich Dense Moisture Cream bundled by Maven Gifts
28. [All Beauty] Old Spice Hair Style Pure Sport Holiday Kit for Men Grooming & Care W/ 2 in 1 Shampoo and Conditioner, Body Wash, Antiperspirant Deodorant, and Men Pomade. Perfect gift for him!
29. [All Beauty] Pacifica Beauty Coco Gloss Shine Hair Serum, Anti-Frizz, Healthy Shine, Fresh Coconut Scent, Silicone Free, 100% Vegan & Cruelty Free
30. [All Beauty] Pacinos Final Touch Hairspray, Anti-Frizz, Firm Hold, Flexible, Fast Drying and Flake Free Aerosol, Add Volume, Texture and Strength to your Hairstyle, Works Against Wind, Moisture and Humidity
31. [All Beauty] Pantene Pro-V Gentle Cleansing with Aloe Vera Extract Shampoo, 10.1 fl oz
32. [All Beauty] Plantur 21#longhair Nutri-Caffeine Women's Long Hair Conditioner with Keratin and Biotin: Strengthen and Nourish, 5.92 fl oz
33. [All Beauty] Privé Blonde Rush Shampoo ( 32 Fluid Ounce / 946 Milliliter ) - Unparalleled Shine to Your Blonde Hair to Keep Your Blonde Catwalk Cool and Fabulous
34. [All Beauty] Quantum Insite (for Delicate Hair)
35. [All Beauty] Renew Eyebrow Revitalizer Eyebrow Growth Oil - All Natural Formula Promotes Natural Hair Growth for Luxuriant Eyebrows - Gently Cleanses and Removes Dead Skin Cells for Healthy Vibrant Hair Follicles
36. [All Beauty] Rock Your Hair Bling it Duo
37. [All Beauty] Roffler Styling Glue Mega Hold Gel 5.1oz (Pack of 2)
38. [All Beauty] Roux 233 Anti-Aging Extra Repair Leave-In Treatment 3-Pack
39. [All Beauty] SC Smart Care Lightening Activator, Powder Lightener For All Stages (0.5 oz 12 Pack)
40. [All Beauty] Scruples Structure Bath Volumizing Shampoo, ER Emergency Repair Conditioner 33.8 oz Set
41. [All Beauty] Sedal Keratina styling cream 300 ml
42. [All Beauty] Shea Moisture 100% Extra Virgin Coconut Oil Head-To-Toe Nourishing Hydration, 10.5 Ounce
43. [All Beauty] TPH by TARAJI Ultra Chill Scalp Serum 4 Fl. Oz! Infused with Aloe, Biotin, Tea Tree Oil, and Caffeine! Refreshing And Revitalizing Scalp Treatment! Sulfate Free, Cruelty Free and Vegan!
44. [All Beauty] The Honest Company Sweet Orange Vanilla Conditioning Detangler Spray, 4 fl. oz. and The Honest Company Everyday Gentle Sweet Orange Vanilla Bubble Bath 12 Fl. Ounces,
45. [All Beauty] The Pomade 3.0 oz
46. [All Beauty] Thrudove Hair inhibitor, Natural Hair Removal, Non-Irritating Painless, Hair Remover, Stop Hair Growth, Hair Inhibiting Hair Growth Inhibitor For Legs Hands Private Part, white
47. [All Beauty] Tweak-d Rare Treasures Self-Cleansing Hair Treatment - Tribal Chocolate 10.58 Ounces by Tweak-d
48. [All Beauty] Urban Hydration Honey Hair Ultimate Style 3pc Set
49. [All Beauty] Vitress Hair Polish
50. [All Beauty] Zach's Wax Color Hair Gel - White - 1 Ounce

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 3
Cluster size: 1170

Representative product titles:
1. [All Beauty] 100% Remy Human Hair Silk Base Top Hairpieces Replacement Clip in Topper For Women Crown Top Piece Long 16''/16inch #6 Light Brown 30g
2. [All Beauty] 10A Body Wave Bundles with Frontal Human Hair Bundles with Lace Frontal Brazilian Body Wave Virgin Hair 3 Bundles with 13x4 Ear to Ear Frontal Closure with Baby Hair (18 20 22 and 16)
3. [All Beauty] 10A Brazilian Straight Hair Bundles Virgin Human Hair 3 Bundles Straight Hair Extensions Weave Hair Human Bundles 100% Unprocessed Virgin Hair Bundles (12 14 16inch, straight 3 bundles)
4. [All Beauty] 16"-22" Tape in Hair Extensions Skin Weft Real Remy Human Hair Straight 20pcs 30g per pack (20"-30g,#6 Light Brown)
5. [All Beauty] 20 Inch Brown Ombre Seamless Clip In Human Hair Extensions, Double Weft Remy Hair Extension Clip On Human Hair, 7pcs, 110g
6. [All Beauty] 6 Packs Pre Stretched Braiding Hair 26 Inch Ombre Professional Itch Free Synthetic Fiber Crochet Twist Braids Hair Extensions (26 Inch, 1B)
7. [All Beauty] 613 Blonde Brazilian Straight Human Hair 13x4 Lace Frontal Andromeda Free Part Ear To Ear Lace Frontal With Baby Hair Pre Plucked Top Swiss Lace Frontal (22" Straight)
8. [All Beauty] 99j Burgundy Bundles Body Wave 4 Bundles with 13X4 Lace Frontal Closure Brazilian Virgin Remy Human Hair Extension with Baby Hair(16 18 20 22 with 16, 99J)
9. [All Beauty] Aonkia Human Hair Dreadlock Extensions for Man/Women Loc Extensions Human Hair 0.2cm Width 18 inch 28 strands Full Hand-made Permanent Dread Locs Extensions Human Hair
10. [All Beauty] Aphro Hair Brazilian Straight Hair Bundles Deals 3 Bundles Brazilian Hair Extensions 100% Unprocessed Virgin Human Hair Weave Bundles Remy Hair Weft 3 Bundles Natural Color （8 8 8）
11. [All Beauty] AuokMar Red Bundles Ombre Human Hair Bundle Extensions For Women 1b99j 3 Tow Tone Black To Natural Brazilian Remy Body Wave Real Weft 12 14 16 Inch
12. [All Beauty] Body Wave Bundles 9A Brazilian Hair Bundles Body Wave Human Hair Bundles 100% Unprocessed Brazilian Body Wave 3 Bundles (24 26 28 Inch)
13. [All Beauty] Body Wave Tape in Hair Extensions 100% Human Wavy Hair 16 inch Long Dark Blonde Soft Remy Hair Skin Weft Seamless Invisible Double Side Tape 20pcs/50g #27
14. [All Beauty] Brazilian Body Wave Hair Bundles with Closure 8A Brazilian Virgin Human Hair 3 Bundles with Closure Free Part 100% Unprocessed Virgin Remy Hair Bundles Natural Color (14/16/18+14)
15. [All Beauty] CHRSHN Clip in Bangs for Women 100% Human Hair Extensions Hairpieces Fringe Air Bangs Wispy Bangs Fringe with Temples Clip on Curved Bangs for Daily Wear（Strawberry Blonde）
16. [All Beauty] Chantiche Italian Yaki 13x4inch Lace Frontal Closure With Baby Hair Brazilian Remy Human Hair Kinky Straight Free Part Full Lace Clsoure Bleached Knots 10Inch Natural Color
17. [All Beauty] Curly Synthetic Ponytail for Black Women, 2 Clips with Elastic Drawstrings Afro Kinky Curly Ponytail Hairpieces Natural Color (12 inch, Large)…
18. [All Beauty] Deep Wave Hair Bundles Human Hair Bundles Natural Black Color Grade 8A Real Unprocessed Virgin Weave Hair Human Bundle Deep Wave Hair 16 18 20 Inch
19. [All Beauty] Down Clip in Human Hair 10" Brown
20. [All Beauty] Eiazalin body wave bundles (18 20 22)
21. [All Beauty] Faux Locs Crochet Hair- 24 inch 6 packs, Knotless Style, Most Natural Faux Locs Crochet Braid, Black Pre-Looped Wavy Twist Crochet Braids Synthetic Braiding Hair Extensions  (24 Inch, 1B)
22. [All Beauty] HEBE 14" Remy Human Hair Clip in Extensions for Women Thick to Ends Dark Brown(#2) 6Pieces 70grams/2.45oz
23. [All Beauty] Huarisi 10A Brazilian Virgin Hair Water Wave 3 Bundles with Closure and Baby Hair Thick Human Hair Weave Extensions 4x4 Lace Closure Free Part Natural Black Color 12 14 16+10inch
24. [All Beauty] IMAYLI Ombre Brazilian Curly Hair 4 Bundles Wet and Wavy Kinky Curly Ombre Human Hair Weave 2 Tone Deep Wave Hair Extensions T1B/30 Color(20202020)
25. [All Beauty] Mariska 10A Body Wave Bundles Human Hair 3 Bundles Unprocessed 100% Brazilian Virgin Hair Weave Bundles Human Hair Bundles Remy Human Hair Extensions (24, Body wave)
26. [All Beauty] Misoun Human Hair Bundle Straight Unprocessed Brazilian Virgin Straight One Bundle 28inch Virgin Human Hair Weave Weft Extension Natural Black Color (100+/-5g)/pc Can be Dyed and Bleached
27. [All Beauty] Neitsi 20" 25s/lot 1g/s 100% Remy Human Hair Nail Lightest Blonde U Tip Hair Extension Natural Wave (613#)
28. [All Beauty] NiegMeag Water Wave Human Hair Bundles 10A Brazilian Virgin Hair Water Wave 3 Bundles 14 16 18 Inch 100% Unprocessed Human Hair Extensions Natural Black Color Can Be Dyed
29. [All Beauty] Ombre Pre Stretched Braiding Hair 24 Inch 3 Packs Brown Synthetic Fiber Croceht Braiding Hair Extension for Twist
30. [All Beauty] PRETTYSHOP Clip In Hair Extensions Full Head One Piece Hairpiece Wavy Heat-Resisting 27" black brown #2 C52-1
31. [All Beauty] Peruvian Short Hair Virgin Body Wave Bundles 50g/Bundles with Closure Bob Weave Human Hair Short Hair Extensions(8"8"10"10"+10"closure)
32. [All Beauty] Real Hair Extensions Clip in Human Hair 18'' Clip in Hair Extensions for Women 7pcs Ombre Hair Extensions Human Hair 120g Remy Hair Extensions(4/27)
33. [All Beauty] Red Human Hair Bundles Ombre Body Wave 3 Bundles 16 18 20 inch Two Tone Black Roots to Red Color Brazilian Remy Hair Weave Double Weft Sew in Hair Extensions
34. [All Beauty] Rosa Star 1-pack 3/4 Full Head Curly Wave Clips in on Synthetic Hair Extensions Hair pieces for Women 5 Clips Hair Extension (16inch, Dark Brown 4#)
35. [All Beauty] S-noilite 23" Long Straight Curly Natural Black 8 Pieces Clip in on Hair Extensions Full Head Set Thick Hairpiece Synthetic Hair Extensions for Girl Lady Women USA Local Post
36. [All Beauty] S-noilite Nano Bead Ring Human Hair Extensions Balayage 18Inch Pre Bonded Nano Tip Hairpieces Cold Fusion Remy Hair 50g 50 Strands For Women #18/613 Ash Blonde/Bleach Blonde
37. [All Beauty] Soft Locs 36 inch 4 Packs Super Long Faux Locs Crochet Hair For Black Women Pre Looped Synthetic Hair Extensions (36 Inch, #30)
38. [All Beauty] Sunny Ombre Micro Beaded in Hair Weft Extensions Real Human Hair Balayage Darkest Brown Ombre Medinum Brown and Light Blonde Real Hair Extensions Micro Weft Brown Double Weft 50g 22inch
39. [All Beauty] Sunwell Weave Hair Human Bundles of Brazilian Hair Extensions Human Hair Bundles Kinky Curly Natural Color 8" 10" 12"
40. [All Beauty] Tape in Extensions Ombre 16 Inch Remy Tape in Hair Extensions Color #6 Brown Ombre to #613 Bleach Blonde Extensions Natural Human Hair 20 Pieces 50 Gram Siky Straight
41. [All Beauty] Tape in Human Hair Extensions Body Wave 20pcs 40g/pack Glue in Remy Hair Dark Brown Invisible Skin Weft PU Tape in Hair Extension 18inch for Women, no Dropping
42. [All Beauty] Top Quality Peruvian Virgin Hair 4 Bundles 50g/PCS with Closure Unprocessed 100% Human Hair Bundles with Lace Closure Peruvian Body Wave(8" 8" 8"8"+10"closure)
43. [All Beauty] U Tip Fusion20.111 Inch- (#Peacock Brown)
44. [All Beauty] Ugeat Hair Extensions Clip in Human Hair Balayage Blonde Hair Extensions Ash Blonde with Platinum Blonde Hair Extensions 7 Pieces Clip in Remy Human Hair 16 Inch 100 Grams
45. [All Beauty] VeSunny 7pcs/120g Ash Brown Balayage Clip in Hair Extensions Color #3 Fading to #8A Mix #18B Clip in Ombre Hair Extensions Remy Human Hair Full Head 22"
46. [All Beauty] Wire Human Hair S Thick 16 Blonde
47. [All Beauty] XYHair 8A Grade Virgin Brazilian Loose Wave Weave Real human ombre hair extensions One Bundle virgin Unprocessed hair bundles Three tone Ombre Hair Color 1B 4 30 100g/pcs(20, ombre 1b/4/30)
48. [All Beauty] Yavida Peruvian Curly Hair 3 Bundles 8A Unprocessed Peruvian Kinky Curly Human Hair Virgin Kinkys Curly Hair Weave Extensions Natural Black Color 12 14 16 Inch
49. [All Beauty] body wave hair 123 (20"22"24")
50. [All Beauty] muaowig Curly Hair 3 Bundle Real Human Hair Natural Black Kinky Curly Hair Bundle Hair Weave For Women Virgin Hair Bundles Extensions For Women 20 22 24 inch, Kinky Curly Hair 3 Bundle

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 4
Cluster size: 229

Representative product titles:
1. [All Beauty] 100% Pure Kolinsky Acrylic Nail Brush Size 12, Oval Crimped Pressed Shaped Nail Art Brush Purple Crystal Handle Acrylic Powder Professional Nail Art Manicure Pedicure Tool for DIY Home Salon
2. [All Beauty] 192W UV LED Nail Lamp,Fast Curing Fingernail Dryer for Gel Polish,Handnail Art Tools,Portable 48 Curing Light Beads handnail Drying Machine with 4 Timer Settings,Auto Sensor for Salon & Home
3. [All Beauty] 3 Pieces Kolinsky Acrylic Nail Brushes Set, Includes 2 Kolinsky Sable Acrylic Crimped Nail Brush for Acrylic Application with Round Red-Wood Handle and Metal Chameleon Cuticle Pusher (Size 8, 10)
4. [All Beauty] 8 Pieces 3D Nail Art Brushes Set Nail Art Liner Ombre Brush Nail Painting Brushes Double Ended Nail Dotting Drawing Pen Acrylic Rhinestone Handles Nail Art Pens
5. [All Beauty] 8 Pieces Cuticle Trimmer with Cuticle Pusher Set Include 4 Stainless Steel Cuticle Nipper Cuticle Remover Dead Skin Pliers 4 Cuticle Scraper Cutter Gift for Women Girls Nail Care (Green)
6. [All Beauty] 8pcs Professional Nail Art Drawing Tool Decoration Finger Design Nail Nail Art Painting Pen Brush Sets White
7. [All Beauty] AIWOGEP Manicure Set, Pedicure Kit, Nail Clippers Cutter, Professional Grooming Kit Made of Precisio Stainless Steel, with gift box, Gifts for man/woman (Blue-18pcs)
8. [All Beauty] Aysekone 1 Set Rose Gold Horse's Head Shaped Nail Tips Holder Fingernail DIY Nail Art Display Stand Magnetic Acrylic Nail Art Practice Stands Nail Art Salon Pillar Manicure Tools
9. [All Beauty] Builder Gel Nail Kit -2 oz Clear&Pink Nail Extension Gel Big Capacity Builder Gel for Nails,Hard Gel Strengthen Set with Nail Forms Brush Nail File DIY for Nail Art Manicure
10. [All Beauty] BuySShow Nail Dryer,Professional 36W Nail Polish Dryer UV Lamp Light,Upgraded with Sliding Tray & Timer Setting + Free Cuticle
11. [All Beauty] Callus Remover Pedicure Kit Set By Onyx - Foot Smoother Buffer, Callus Rasp, Foot File, Nail Clipper, Foot Lotion
12. [All Beauty] Callus Remover,Bienna Electronic Foot File Pedicure Tools [Rechargeable] [Waterproof] Electric Professional Shaver for Dry Dead Cracked Hard Feet Skin Calluses with LED Light and a Extra Grinding Head
13. [All Beauty] Citre Shine Shine Mist Laminator 3 oz. Pump (3-Pack) with Free Nail File
14. [All Beauty] Ckeyin ® Brand New Waterproof Rechargeable Electric Callus Remover Grinding Pedicure Kit/ Foot Spa Smoother - Frustration Free Packaging
15. [All Beauty] CreazyDog 1Pc Nail Art Orange Wood Stick Cuticle Pusher Remover Pedicure Manicure Tool
16. [All Beauty] EZGO Professional Beauty Care Nail Files Double Sided Nail Block Buffer Shiner Nail Buffer and Shine Kit - Manicure Polishing Nail File for Natural Nails (6PCS)
17. [All Beauty] Electronic Foot File Professional Pedicure Tools Foot Care Callus Remover for Dead Hard Cracked Skin on Feet Include 2 Mineral Pumice Stone Rollers and Massage Roller Head
18. [All Beauty] Expert Touch Lint Free Nail Wipes - 475pcs - 1 Box
19. [All Beauty] GGYao Manicure Set Nail Clipper Set, Fingernails & Toenails Clippers with Luxurious Leather Case, Stainless Steel Personal Care Tools Nail Scissors - 10 pieces (Blue)
20. [All Beauty] Gel Nail Polish Acrylic Steamer Remover Portable Harmless Nail Machine Nail Art Tools BLUETOP (Electric,White)
21. [All Beauty] HOMIEHOME Electric Nail File Care System-Professional Powerful Manicure/Pedicure Tool for Hands Salon SPA At Home
22. [All Beauty] JODSONE 30000RPM Portable Nail Drill Machine, Electric Nail File for Acrylic Nails, Portable Efile Nail Drill Manicure Pedicure Tools Easy to Insert & Remove Drill Bit
23. [All Beauty] KADS Nail Art Paint Pen Diamond Crystal Dotting Fountain Pen Brush DIY Nail Art Manicure Tool with 5 Replacement heads
24. [All Beauty] LED Nail Lamp - 80W Gel Nail Dryer with 4 Timer, Sensor - Professional Curing Light for All Gel Nails and Toe Nail Curing
25. [All Beauty] LOCONHA Foot Files Callus Remover, Stainless Steel Foot Rasp and Professional Foot Scrubber Pedicure Kit
26. [All Beauty] LOHOME Portable Electric Nail Drill - 9 in 1 Nail File Kit Grinder Manicure Machine Battery-operated Nails Portable Salon Machine for Nail Polishing Grinding
27. [All Beauty] Lip Plumping Microneedle Roller System by ORA for Unisex - 0.25 mm Needle
28. [All Beauty] Lisapack 4PCS Empty Nail Polish Corrector Pen, Nail Polish Remover Pen for Cleaning Nail Art, Paint (White)
29. [All Beauty] MAKARTT Detachable Nail Brushes Set UV Gel Acrylic Nail Art Design Builder DIY Flat Brush Pen Set
30. [All Beauty] Manicure Set 3 In 1 Stainless Steel Professional tip nail clippers for thick Pedicure Nail Clipper Cutter black light
31. [All Beauty] Meao 16 Pcs Magnet Bar Nail Art Tool Magnet Stick Wand Set for 3D Cat Eye Effect Powder - Ideal Manicure UV Gel Nail Polish DIY Magnetic Design Pen Gadget
32. [All Beauty] NAIL-AID Magic Callus Remover, Clear, 5.5 Fluid Ounce
33. [All Beauty] NMKL38 7PCS Ombre Nail Design Brushes, UV Gel Nail Drawing Painting Brush Pen Set with Nylon Hair Acrylic Handle, Professional Nail Art Tool
34. [All Beauty] Nail Art Brushes Set Acrylic Nail Brush Professional UV Gel Nail Brush Pen Set 9pcs
35. [All Beauty] Nail Drill Bits Set - 12PCS Includes Diamond/Silicone/Brush/Ceramic Nail Drill Bit - Single Packed 3/32" (2.35mm) Nail Bits for Acrylic Gel Dip Powder Natural Nails Polishing and Cuticle Clean
36. [All Beauty] Nail Envy Treatment Breakfast at Tiffany's On The Go Kit " 3 piece set " + Free Cuccio Butter Tuscan Citrus Herb .33oz each.
37. [All Beauty] Nail Files, ReachTop 20 Pack Black Professional Washable Nail Buffer Double Sided 100 180 Grit Sanding Buffers Emery Boards for Home Salon Art Pedicure Manicure Tools
38. [All Beauty] Nail Soaking Bowl Electric Multi-mode Vibration Massage Nail Spa Bowl Soften Cuticles Nail Art Manicure Bowl Relaxing Treatment Nail Soak Off Bowl for Gel Nails
39. [All Beauty] Portable Nail Curing Lamp Led Nail Dryers for Gel and Regular Polish with Sensor for Acrylic Nails, Nail Dryer Light Curing Lamp (pink)
40. [All Beauty] Pretfarver Pedicure Foot File for Feet Hard and Dead Skin with 3 Extra Rollers Electronic Professional Spa Foot Care Tools Rechargeable Callus Remover
41. [All Beauty] Professional 15pcs Stainless Steel Manicure Set Nail Clipper Set Nail Tools with Portable Travel Case
42. [All Beauty] Silicone Needle for Men,Black(2Pcs,2 Sizes)
43. [All Beauty] Sularpek Dotting Tool Set, 5 Pcs Embossing Stylus with Double Sized Ball Tips, Ball Embossing Stylus for Transfer Paper, Tracing Tools for Drawing
44. [All Beauty] Vashion Cuticle Pusher- Double headed Stainless Steel Triangle Gel Nail Polish Remover Cuticle Peeler with Scraper
45. [All Beauty] WerkaSi Nail File 100/180 Grit Nail Buffering Files Professional Manicure Pedicure Tools 8Pcs
46. [All Beauty] Winstonia Nail Art Brush Tool Cleaning Cleaner Cup Jar Container with Multiple Size Slots and Lid
47. [All Beauty] Yimart Bundle Monster New Pro Nail Art Design Painting Detailing Brushes & Dotting Pen Kit Set Pack of 20
48. [All Beauty] Yimart Manicure Pedicure Set Nail Clippers Kit Nail Tools Stainless Stee Nail Scissors Grooming Kit of 18pcs with Travel Case(Rose Red)
49. [All Beauty] Yimart® Pack of 20,Nail Art and Gel Acrylic Drawing Painting Brush Set with Dotting Pen Tools (G)
50. [All Beauty] iBelieve 30000RPM Professional Nail Drill Machine, 3 in 1 Detachable Electric Nail Drill Set for Acrylic Gel Nails – Nail Dust Collector/LED Desk Lamp/Nail Drill Bits

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 5
Cluster size: 261

Representative product titles:
1. [All Beauty] 10 Pcs Silicone Travel Bottles Set, Travel Size Containers, Leak Proof Squeezable Tubes with Keychain and Retractable Badge Holders, Reusable Bottle for Toiletry, Shampoo, Liquid, Cosmetic (1.3 Oz)
2. [All Beauty] 12 Pieces 2 ml Empty Lip Gloss Tubes Containers Clear Refillable Lip Balm Bottle Transparent Lip Gloss Containers Plastic Lip Balm Tube Bottle with Rubber Insert for DIY Lipstick Makeup Cosmetic
3. [All Beauty] 16 Pieces 5 ml Mini Leopard Design Empty Lip Gloss Tube Plastic Lipstick Sample Bottle Refillable Lip Balm Container with Inserts and 4 Pieces Funnels for Women Girls Cosmetic Liquid Travel Home
4. [All Beauty] 16oz 500ml Empty Plastic Spray Bottles for Cleaning Solutions Tattoo Flower Mist Bottle Hair Salon Tool Hair Dressing Refillable (1)
5. [All Beauty] 18 Pieces Empty Travel Size Bottle with Keychain Holder Set, Includes 6 Reusable Refillable Flip Cap Bottle 30 ml, 6 Keychain Holder Pouch, 6 Wristlet Keychain Lanyard for Soap Liquid Toiletry
6. [All Beauty] 20 Pcs Lip Gloss Tubes Empty Balm Bottles Lip Balm Tubes for DIY Cosmetic Sample Containers
7. [All Beauty] 20 Pieces 10 ml Empty Mascara Tube Refillable Eyelash Wand Tube Plastic Eyelash Cream Container Bottle with 20 Rubber Insert and 4 Plastic Funnel for DIY Cosmetic Oil (Gold, Silver, Rose Gold, Black)
8. [All Beauty] 2oz / 60ml Glass Spray Bottles for DIY Refill, Essential Oils, Pillow Mists,Fine Mist Spray -3Packs Amber Color
9. [All Beauty] 30 Pieces Hand Sanitizer Keychain Holders 10 Empty Travel Size Bottle with Flip Cap 1oz Container 10 Reusable Bottle Holders 10 Wristlet Keychain for Backpack and Purse(Multiple Patterns)
10. [All Beauty] 6 Pack Clear Plastic Pump Bottle 16oz
11. [All Beauty] Act Braces Care Size 18z Act Braces Care 18z
12. [All Beauty] Beyond the Zone Color Shotz Purple Passion Purple Passion
13. [All Beauty] Bourjois Volume Glamour Push up Black Serum
14. [All Beauty] Cake Desserted Island Supreme Body Mousse 30ml/1oz Travel Size
15. [All Beauty] Clear Glass Cotton Swab Q-Tip Holder/Alcohol ISO Station 2.5"
16. [All Beauty] Coppertone Spf#70+ Kids Wacky Foam 6 Ounce (177ml) (3 Pack)
17. [All Beauty] Deb Stoko Solopol Classic 83187 Heavy Duty Hand Cleaner (2000 ml Soft Bottle) (1 Bottle)
18. [All Beauty] Disney Planes Mini Gift Set with 4 Miniature Eau De Toilettes
19. [All Beauty] Dr. George's Plaque Blast
20. [All Beauty] Driew Pump Bottle, Pump Bottles for Shampoo 17oz Pack of 2 (Green with White Pump)
21. [All Beauty] Flavor Plus Oral Suspending Vehicle 16 oz
22. [All Beauty] Frcolor 2pcs 550ml Empty Spray Bottle Multi-functional Plastic Spray for Home Garden (Assorted Colors)
23. [All Beauty] Glass Spray Bottles Empty 16oz Boston Round Bottle Refillable Container for Essential Oils with Funnel Lables Cleaning Products Aromatherapy Lotions Liquid Soaps (BrownSilver)
24. [All Beauty] Gücci Bamboo EDP Rollerball 0.25 oz
25. [All Beauty] H42 Clipper Cleaner 16 Oz. Jar Virucidal Anti-bacterial by H-42
26. [All Beauty] Halloween L 4pc Set (3.4 SPR + 5.0 Bl + 5.0 Sg + Mini) Set
27. [All Beauty] KANECHOM LEAVE-IN COND KARITE 300ML(10OZ) - Set of 2
28. [All Beauty] LIQUID LNR BLAST BROWN BLAZE
29. [All Beauty] Label M Miracle Fibre 50 ml by Label M
30. [All Beauty] Life Extension Ultra Prostate Formula, Softgels, 60 Count (Pack of 3)
31. [All Beauty] Lip Balm Containers, 25 White Chapstick Tubes, BPA Free, Make Your Own Lip Gloss - 0.15oz, Made In the USA
32. [All Beauty] Listerine Cool Mint Antiseptic Mouthwash, Bad Breath, Plaque & Gingivitis, Mint, 1.5 L (Pack of 3)
33. [All Beauty] MISAZ 10 Pieces Empty Lipgloss Bottle Tube Refillable Lip Balm Bottles Plastic Lovely Ice-cream Shaped Cosmetic Samples Container DIY Lip Glaze Vials for Travle Women Makeup Girls Beauty,5ml/0.2oz
34. [All Beauty] Menn Speed Stick Regular Size 3z Menned Speed Stick Regular 3oz
35. [All Beauty] Milas Oloves Lemony Lover -- 1.1 oz Each / Pack of 10
36. [All Beauty] MoYo Natural Labs 8 oz Spray Bottles, Trigger Sprayer Empty Travel Containers, BPA Free PET Plastic for Essential Oils and Liquids/Cosmetics (3 pack, Candy Pink)
37. [All Beauty] MoYo Natural Labs Turret Spout 8 oz Empty Liquid Bottle with Adjustable Dispenser (Pack of 2, Clear)
38. [All Beauty] OKAY Tube colored edges black tube 0.5oz
39. [All Beauty] Premium Quality New Empty Clear Plastic Cosmetic Containers 5 Gram Size Jars Pot Eyeshadow Container Lot Size: Diameter: 1 1/4" inch X Height: 3/4 inch. (Comes With 1 Free Myo Eyeshadow Sample) (10 Pieces)
40. [All Beauty] Purell Instant Hand Sanitizer Refills, Unscented, 2000 mL Refill Bags, Case of 4
41. [All Beauty] R&B Phyton Therapy Herb Moisture Glaze 15.87oz
42. [All Beauty] ReliaMed Ostomy Odor Eliminator Drops 8 oz. Bottle (Each) (Bottle of 8 Ounces) by ReliaMed Misc.
43. [All Beauty] SWEEN 24 CREAM 5 OZ TUBE (EA) by genius.nn
44. [All Beauty] Santa Maria Novella Acqua di Colonia - Melograno 3.3oz
45. [All Beauty] Scruples Enforce Sculpting Glaze Extra Firm 1000 ml / 33.8 oz
46. [All Beauty] Sec Outlst Inv Sld Pwdr P Size 2.6z Sec Outlst Inv Sld Pwdr Prtct 2.6z
47. [All Beauty] Silicone Travel Bottle Leak Proof Soft Squeezable Refillable Travel Containers,37ml/1.25oz,set of 4 Color
48. [All Beauty] Teensery 5 Pcs 4ml Empty Clear Mascara Tube Eyelashes Wand Tube Vials Bottle Container With Plug
49. [All Beauty] Vine Vera Cabernet High Potency Collection 60 Seconds Eye Solution
50. [All Beauty] [SNP] Ampoule Mask 25ml Pack of 10 (5 Type x 2)

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 6
Cluster size: 774

Representative product titles:
1. [All Beauty] (3 Pack) RIMMEL LONDON Stay Matte Liquid Mousse Foundation - True Ivory
2. [All Beauty] 3 x Max Factor Creme Puff Face Powder 21g New & Sealed - 05 Translucent
3. [All Beauty] American Beauty Ultra-Easy Automatic Lipliner - 04 Butterscotch
4. [All Beauty] Aveda Uruku Lip Pigment - Lipstick - #70 Sheer Ochre
5. [All Beauty] Beauty Eyeshadow Palette Matte Makeup,Glitter Eyeshadow Palettes Vegan,Professional Shimmer Eye Shadow Pallet,Purple Red Orange Smokey Pink Natural Warm Pigmented (12 Colors Eyeshadow Palette Matte)
6. [All Beauty] Benefit Cosmetics Stay Flawless 15 - Hour Primer
7. [All Beauty] Best Skin Care Makeup Shimmer Powder - Alexis Vogel After Glow - Create Beautiful Youthful Skin Glow - Use After Moisturizer with Highlighter Makeup, Contouring Makeup, Bronzer, or Blush - Created by Celebrity Makeup Artist
8. [All Beauty] Candylipz Red Single Lobe
9. [All Beauty] Cat Eye Liner Suede,Jordana Cosmetics,Co-07
10. [All Beauty] ColourPop - Pressed Powder Highlighter (S'il Vous Play)
11. [All Beauty] DE'LANCI 10 Colors Cream Concealer Contour Palette Pro Face Concealer Highlighting Contouring Kit Complete Coverage Camouflage Concealer Cosmetics Set with Mirror Make Up Brush Tool
12. [All Beauty] EYE MAJIC INSTANT EYESHADOW – INSTANT BEAUTY PROFFESIONAL MAKEUP IN 10 SECOND (5 Pair Pack, Matte 107 - Romanesque)
13. [All Beauty] FOCALLURE Translucent Loose Face Setting Powder,Long-lasting Oil Control Waterproof Sweat-proof Concealer without Makeup Powder, Beauty Make Up for Light and Dark Skin Tones
14. [All Beauty] Femme Couture Velvet Eye Colour Velvet Champagne
15. [All Beauty] I'M MEME I'M Heart Stamp Blusher | Blendable Cushion Blush with a Matte Finish | Fun Makeup for Teens | 001 Beloved Red | Korean Makeup, K-Beauty
16. [All Beauty] Jeffree Star x Manny MUA Limited Edition Skin Frost ~ Eclipse
17. [All Beauty] KKW BEAUTY Powder Contour and Highlight Kit Light
18. [All Beauty] KRISTOFER BUCKLE Cashmere Slip® Longwear Lipstick Duo, 0.11 oz. (each) | Creamy, Richly Pigmented Lipstick That Delivers Bold Color for Up To 8 Hours | Bardot/Doll
19. [All Beauty] Labello Soft Rose, Labello Watermelon Shine, Labello Cherry Shine Lip Balm Bundle
20. [All Beauty] Lasting Makeup Foundation – Face&Body Liquid Foundation Lightweight Bottle Full Coverage Invisible Pores Covering Blemishes - for All Skin Types (40 mL)
21. [All Beauty] Lime Crime Metallic Velvetines Long Lasting Liquid Matte Lipstick - Seashell Bra
22. [All Beauty] Loose Highlighters (1)
23. [All Beauty] Lurella Liquid Lipstick Fade
24. [All Beauty] M.A.C Selena La Reina - Edition 2020 - Extra Dimension Skinfinish - Color La Leyenda
25. [All Beauty] MAC Frost Lipstick - New York Apple
26. [All Beauty] MAC IRIDESCENT POWDER JUSTINE SKYE
27. [All Beauty] MILANI HD Advanced Lip Color-MLMHL116 Raspberry Blush
28. [All Beauty] Marine Forest Lip Liner and Lipstick Set, Matte Lip Gloss Makeup Kit, Nude Non Sticky Waterproof Long Lasting Liquid Lipstick (Stone)
29. [All Beauty] Milani Bella Eyes Gel Powder Eyeshadow Satin Matte - 04 Bella Caffe (Pack of 2)
30. [All Beauty] Milk Makeup KUSH Lip Glaze - Nova
31. [All Beauty] Mineral Hygienices Bronzer Warm Kiss 28g
32. [All Beauty] Mineral Hygienics Matte Finishing Powder 38g
33. [All Beauty] Mountain Ocean Skin Trip Lip Balm – Three 0.165 Ounce Tubes
34. [All Beauty] NARS Women's Cheek Palette, Orgasm/ Laguna/Mistinguette/Goulue, 0.12 oz
35. [All Beauty] NYC Expert Last Lipcolor - Love My Latte
36. [All Beauty] NYX PROFESSIONAL MAKEUP Stay Matte but not Flat Liquid Foundation, Medium Beige, 1.18 Fluid Ounce
37. [All Beauty] Nourishing Lip Balm 0.5 oz by Diptyque
38. [All Beauty] Nuance Salma Hayek Flawless Finish Illuminating Blush & Bronzer Duo with Argan Oil #560 Bronzed Rosewood
39. [All Beauty] O.TWO.O Magical Concealer Stick Foundation Makeup Full Cover Contour Face Concealer Cream Base Primer Moisturizer Hide Blemish (06wheat)
40. [All Beauty] PAT McGRATH LABS Skin Fetish: Divine Powder Blush Divine Rose
41. [All Beauty] ROESIA Rose cosmetics High Pigment eyeshadow palette, natural eyeshadow palette, natural colors eyeshadow palette, waterproof eyeshadow palette,shimmer eyeshadow palette
42. [All Beauty] SEPHORA COLLECTION Rouge Gel Lip Liner 10 cactus flower 0.0176 oz
43. [All Beauty] Studio Gear Celebrity Eyeshadow
44. [All Beauty] Temporary Tooth Color Alcohol Activated Palette, Decay
45. [All Beauty] Ulta Velvet Blush 0.12 Oz. Princess (pink mauve with shimmer).
46. [All Beauty] Wanderlust Powder Foundation Medium (medium with warm, subtle olive undertones)
47. [All Beauty] [KARADIUM] PUCCA LOVE EDITION Shine Eye Shadow 1.7g - 6 Colors / Long Lasting Moist Fitting Daily Makeup Shadow (#06 SMOKY SHINE)
48. [All Beauty] anitotuwan Air Cushion CC Cream Mushroom Head Moisturizing Foundation Matte Concealer BB Cream Primer Base Makeup, with Mushroom Head Makeup Sponge
49. [All Beauty] e.l.f. Cosmetics Primer-Infused Blush Always Spicy 0.35oz, pack of 1
50. [All Beauty] onamor 5PCS 3D 𝐌𝐀𝐒𝐊 Bracket Inner Support Lipstick Protector, Large Size for Adults

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 7
Cluster size: 827

Representative product titles:
1. [All Beauty] 30g Pore shrink cream Face Moisturizers Magical Perfecting Base Face Primer Under Foundation Complexion Skin Cream Pores Relieving Dryness Oil Control Firming Moisturizing
2. [All Beauty] BABOR Power Serum Ampoule: Beta Glucan | Calms, Strengthens, Soothes | 2D Hyaluronic Acid & Microsilver | Clean & Vegan | Visible Results in 7 Days
3. [All Beauty] Baby Skin by Maybelline Instant Cheek Flush Flirty pink
4. [All Beauty] Bellissima Beauty Care - Jade Roller and Guasha Stone with Compressed Face Mask for Complete Facial Treatment Anti-Aging, Natural Jade Stone for Face and Body Massage, Diminish Fine Lines & Wrinkles
5. [All Beauty] Bolton's Naturals Magnesium Chloride Balm (Lavender)
6. [All Beauty] Bulldog Essential Skincare Kit for Men Original Products
7. [All Beauty] Bye Bye Blemish Drying Lotion Proven Spot Treatment Acne Repair, Overnight Results size 1 fl oz / 29.5 ml
8. [All Beauty] CELDERMA Real Moisture Flower Hydrogel Mask Pack (5-sheet)
9. [All Beauty] Cabana Cream Hydrating Body Gloss 6 oz.
10. [All Beauty] Codream Moisturizing Gel Heel Sleeves and Gloves, Gel SPA Gloves Socks Repair Cracked Skin and Exfoliate Skin,Soften Beauty Hands and Feet for Women
11. [All Beauty] Decollette Pad Wrinkles Remover Chest Patch (Applies Clear) (2 Pack) Silicone Wrinkle Prevention Pads Hypoallergenic Patches Fine Line Corrector Reducer - Anti Aging Natural Products - 5" x 5.5"
12. [All Beauty] Dermasil Dry Skin Treatment Original Lotion 14.5 Fl Oz (14.5)
13. [All Beauty] Hair Growth Inhibitor and Moisturizer Cream, Stop Facial Body Leg Hair Growth for Women Men, Non-Irritating Painless Hair Removal Inhibitor for Armpit, Keep Your Skin Smooth and Moisturizing
14. [All Beauty] Hippie Skin Hippie Everyday Bundle Cleanser Moisturizer Toning Spray Oil Cleansing Method, Makeup Remover, Makeup Primer, Powerful Natural Skin Care for all Skin Types
15. [All Beauty] Hyaluronic Acid Serum for Face - Topical Moisturizing Facial Serum Boosts Hydration for Smooth, Supple Skin. Natural Anti Aging Formula Includes Aloe Vera, Jojoba Oil and Witch Hazel. Made in the USA
16. [All Beauty] Hylunia - Reconstructive Crème - Psoriasis Eczema Severe Dryness (shea butter formula) 4 fl. oz. / 118 ml.
17. [All Beauty] Hylunia Anti-Stress - Ojas 1.0 oz
18. [All Beauty] Innisfree Red Beet Bright Toning Cleanser 100ml New Super Food Skin Care Line/Transparent skin and Moisture Care
19. [All Beauty] Isme Pueraria Mirifica Powder for Beauty & Firming Face Skin 80 G.
20. [All Beauty] It'S SKIN The Fresh Face Mask Sheet Rose | Natural Moisturizing Korean Face Mask Beauty for All Skin Types | Day and Night Moisturizer for Face w/ Vitamin C & A | Glass Skin Face Mask Skin Care Sheet (1 EA)
21. [All Beauty] Jergens Naturally Smooth Shave Minimizing Moisturizer - 9.9 fl oz
22. [All Beauty] Jewelry Base Ruby Moisturizing Nourishing Makeup Base Serum- Great for Dry Sensitive skin, 55ml
23. [All Beauty] Joey New York Correct-A-Line for Face 1.59 oz.
24. [All Beauty] Mama's Gold Stretch Mark Prevent Oil 8oz (FFP)
25. [All Beauty] Marc Jacobs Youthquake Hydra-full Retexturizing GEL Creme Moisturizer 50ml
26. [All Beauty] Marvel Avengers, Pure Sun Defense, SPF 50, For Sensitive Skin, Broad Spectrum, 8 oz
27. [All Beauty] Mother’s Select Stretchmark & Cellulite Complex for Women Thighs, Legs, Stomach, Pregnancy, Slimming, Firming, Removal, Tightening, Hydration, Unsightly Scars, & Fat Deposits
28. [All Beauty] Nu-Pore Moisturizing Face Mask - Face Masks for Women and Men With Vitamin E Oil and Green Tea for Hydrating, Toning and Soothing Sheet Masks, 2 Pairs Per Pack (24 Pack)
29. [All Beauty] Omar Sharif a.c.care Water Essence 120ml
30. [All Beauty] PLANT ØÅ Face Oil - For Normal/Combination Skin
31. [All Beauty] PRIOR Gel Serum Refill Shiseido
32. [All Beauty] Pain Relief Cream with Menthol and Arnica - Cooling Gel Medication for Back, Knees, Elbows, Muscles, Arthritis & More - Powerful Anti Inflammatory Treatment for Lasting Relief - InstaNatural - 2 OZ
33. [All Beauty] Parisian Secret Revitalizing Moisturizer
34. [All Beauty] REVIVA LABS - Ultra Rich Ultra Light Daytime Moisturizer w/ Vitamin C (Packs of 2)
35. [All Beauty] ROPALIA 1PC Blackhead Remover Deep Cleansing Peel Off Acne Black Mask Mud Face Mask
36. [All Beauty] Reusable Silicone Face Patch Set - 5 Wrinkle Patches for Overnight Fine Line & Crease Flattening - Forehead, Under-eye and Smile Lines Repair
37. [All Beauty] SKIN 1004 Madagascar Centella Soothing Cream 1.01 fl oz(30ml) | Quadruple Ceramide Complex | Strengthens Skin Barrier | Smooths Skin
38. [All Beauty] SPAScriptions Brightening SPA Treatment Mask, 5 masks
39. [All Beauty] Sangeo Day/Night Collagen Serum To Enhance Complexion- Deeply Hydrate- Diminish Fine Lines and Wrinkles
40. [All Beauty] Silicone Sponge Applicator for Makeup and Tanning Lotion - Flawless Coverage for ALL Skin Types, Latex-Free, Non-Toxic
41. [All Beauty] Skincare Retinol Skin Brighten Er 1oz (3 Pack)
42. [All Beauty] Stemulation Daily Micro Derm Scrub - Gentle Exfoliator Scrub For Face And Body - Aloe Based Antioxidant Complex For Refined Healthy Skin
43. [All Beauty] Supergoop SPF 30+ Endless Summer Pump
44. [All Beauty] Toner With Tea Tree & Lavender Essential Oil Facial Treatment | Alcohol, Acid-Free, Filler Free 100% Natural Ingredients | Reduce Breakouts, Acne, Blackheads, Shrink Pores, Tighten Facial Skin | 100ml - REVERENCE NATURALS
45. [All Beauty] Topwon 4.5Inch Makeup Remover Pads Washable Cotton Face Cleansing Pad for Sensitive Skin 3 Packs Facial Washing Puffs to Remove Mascara Foundation Lipstick
46. [All Beauty] VB Beauty Miracle Eye Creme Set
47. [All Beauty] Vegan Face Foaming Cleanser by ATHÉ Authentic Pink Vita Foaming Cleanser 6.08oz, 180ml | Athe Foaming Cleanser | Energy of Pink Vitamin and the Peeling Effect of Konjac Jelly | Vegan Face Foaming Cleanser | Vegan Deep Cleansing | Kbeauty
48. [All Beauty] Vitamin C Serum for Face & Eyes by Skin Glow Naturals - Topical Skin Care with Vitamin C & E, Hyaluronic Acid and Organic Ingredients - Perfect for Anti-Aging, Wrinkles and Acne - 1fl oz
49. [All Beauty] XUANAI Automatic Heating Wand Massager with 12 Powerful Speeds & Astonishing Vibration Modes (Pink-)
50. [All Beauty] [ditebeau] Honey Jam Mask 25g x 10ea

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 8
Cluster size: 139

Representative product titles:
1. [All Beauty] 10 x French, Chevron & Teardrop Nail Tip Guides Stickers (Pack of 10) NEW Style
2. [All Beauty] 12 Colors Nail Glitter Sequins Maple Leaf Nail Art Sticker Holographic Flakes Diy Nail Decorations Decals for Thanksgiving Nail Confetti Decoration Supplies Manicure
3. [All Beauty] 12 Pack Bollywood Head Bindi Tattoo Nail Bling Art Rhinestone Stick On Reusable
4. [All Beauty] 160 Pieces Full Wraps Nail Art Polish Stickers Self-Adhesive Nail Strips Solid Color Gradient Glitter Design Nail Decals Accessories Manicure Kits for Women Girls DIY Nail Art Designs 10 Sheets
5. [All Beauty] 2 Packs Nail Sequin Nail Glitter Sequins Mixed Paillettes Holographic Nail Art Sparkly Glitter Sheets Tips Manicure Nail Decoration for Nail Crafts Face Eyes Body (Iridescent Mermaid, Butterfly)
6. [All Beauty] 24 Sheets Full Nail Art Stickers Spring Leaf Flowers Designs Water Transfer Watermark Stickers Flamingo Nail Decals Thanksgiving Nail Wrap Manicure Stickers for Women Girls DIY Fingernail Decorations
7. [All Beauty] 2600 Pieces Round Glass flatback Nail Rhinestones With Nail File Pick Up Pen And Crystals Gems,Mix 7 Sizes Flat Back Crystal Stones For Nails Art Decoration DIY Crafts Clothes Shoes（Gold Rose）
8. [All Beauty] 300 Pcs Nail Art Acrylic Nail/UV GEL Nail Extension Tips Form Guide Sticker（Horse eye shape）
9. [All Beauty] 3D Gold Metal Nail Studs- Nail Gold Rivets for Nail Art Geometric Circle Oval Heart Triangle Square Shaped Nail Art Decorations with 1Pcs Tweezers And 1Pcs Picker Pencil
10. [All Beauty] 3D Micro Nail Caviar Beads Mixed Color Nail Art Supplies Set 4 Boxes 0.4mm Small Nail Studs Charms for Nails Beauty Nail Art Accessories
11. [All Beauty] 5Pcs/Set Acrylic Nail Design Practice Stands Magnetic Nails Holders Training Fingernail Display Stands DIY Nail Crystal Holders for for False Nail Manicure Tool Home Salon Use Nail Art Accessories Ra
12. [All Beauty] 7 Sheets French Nail Stickers for Nail Art Supplies French Tips Nail Decorated for Acrylic Nails 3d Self-Adhesive Nail Design Line Nail Decals for Women Girls Gold Designer Nail Stickers Manicure Tips
13. [All Beauty] 8 Sheets Graffiti Nail Art Stickers Decals,3D Self Adhesive Fun Doodle Rainbow Human Face Nail Design for Women Girls Kids,DIY Acrylic Nail Supplies Nail Decoration
14. [All Beauty] ANGNYA 8 Pcs Nail Rhinestones Picker Wax Replacement Head Tips for Nail Dotting Pen Beads Rhinestones Dual Ended Wax Nail Rhinestones Picker Replacea Nail Accessories with Case
15. [All Beauty] Autumn Fall Leaves #5 Nail Art Decals
16. [All Beauty] BFY Christmas Nail Foil Transfers Stickers Nail Art Supplies 10 Pcs Santa Claus Snow Bell Christmas Tree Nail Decals Tips Wraps Nail Art Accessories for Women Christmas Decor DIY Nail Art
17. [All Beauty] BMC 120pc Flexible Gold Metal Fleur De Lis Cut Out Nail Art Decorative Confetti
18. [All Beauty] BMC Nail Art Water Transfer Tattoo Effects Decoration Decal-Peacock French Tips 2
19. [All Beauty] Chakras - Waterslide Nail Decals - 50pc
20. [All Beauty] Christmas Nail Foil Transfers Stickers Nail Art Decor 4 PCS Xmas Styles Nail Stickers Snowflake Elk Starry Santa Claus Nail Applique Mix Pattern Design for Women with Christmas Party
21. [All Beauty] Duufin 10 Boxes Nail Sequins Colorful Nail Art Glitter Confetti Holographic Shining Nail Flakes 3D Laser Thin Star Heart Glitter Sequin for Nail Art Decoration with 1 Pc Tweezers and a Nail Brush Pen
22. [All Beauty] Flamingos Nail Art Stickers Decals 3D Gold Designer Nail Decals Flamingos Letter Nail Art Supplies 6 Sheets Nail Stickers Self-Adhesive Designer Nail Stickers Nail Decorations Acrylic Nail Art
23. [All Beauty] GGSELL JK 16 pcs nail art Nail patch nail stickers nail foil Merry Christmas Snowball snowflake decoration
24. [All Beauty] Generic 1 Sheet Flower 3D Nail Art Stickers Silver Lace Pattern Stamping Nail Tips Stamping Decals
25. [All Beauty] Gold Dragon Snake Nail Art Stickers Decals Acrylic Nail Supplies Designer 8Pcs Nail Sticker for Nail Art Rose Flower Bee Stars Moon Retro Fashion Luxury 3d Self-Adhesive Nail Accessories Decorations For Women Girls (Gold)
26. [All Beauty] Halloween Nail Art Foils Fall Nail Foil Transfer Stickers, 10Rolls Holographic Nail Foil Decals Nails Art Supplies Halloween Pumpkin Skull Spider Web Ghost Design Sticker for Manicure Tips Decorations
27. [All Beauty] Heart Banner Nail Stickers - Valentines Nail Art (Pink)
28. [All Beauty] Holographic Mermaid Nail Glitter Sequins, Colorful Confetti Sticker Manicure Nail Art Supplies Make Up DIY Decals , for Body Face Hair Make Up Nail Art Mixed Color Glitter Decoration
29. [All Beauty] Konad Set Starter Kit for Stamping Nail Art (C-B SET)
30. [All Beauty] Marble Nail Decals Water Transfer Nail Stickers for Nail Art Designer Supplies 12 Sheets Nail Art Stickers for Acrylic Nails Beauty Nail Decoration Kits Water Decals Nail Decors Women Kids Girls Nail Accessories
31. [All Beauty] NAIL ANGEL 12pcs Nails Strips Nail Art Wrap Nail Art Full Cover Sticker Leopard Prints Sticker Fashion Designs for Women (10153)
32. [All Beauty] NAIL ANGEL 16 Sheets Nail Art Water Decals Water Transfer Sticker Different Painting Pattern Decals for fingernail and toenail Manicure (16sheets) 10080
33. [All Beauty] NAIL ANGEL 7pcs/Pack Nail Art Pure Color Wrap Full-Cover Finger Nail Sticker 16tips/Sheet Nail Strips for Women 10089 (10089)
34. [All Beauty] Nail Art Stickers Accessories for Girls Beach Mermaid Decorative Nail Decals for Women Summer Series Sea Animal Seagull Flag 3D Nail Sticker Wraps for Kids Fingernails & Toenails Decoration Manicure
35. [All Beauty] Nailart NAIL TATTOO STICKER - turtle / tortoise - pink
36. [All Beauty] Polytree 12 Colors DIY Nail Art Glittering Rhombus Sequins Manicure Decorations
37. [All Beauty] Polytree 12 Colors Fashion 3D Square Nail Art Decor Bling Rhinestone DIY Tips Wheel
38. [All Beauty] Retro Style Chunky Finger Ring In Anti Silver Colour and Big Oval Turquoise Stone In Ornamented Decorative Mounting
39. [All Beauty] SPECIAL SET small - Nailart NAIL TATTOO STICKER - comic / cartoon / bee / bumblebee - yellow / black / blue
40. [All Beauty] SPECIAL SET small - Nailart NAIL TATTOO STICKER - turtle / tortoise - green
41. [All Beauty] Self Adhesive Resin Rhinestones Picker Pencil Nail Art Gem Crystal Pick up Tool Wax Pen Long 10Pcs with 3 pcs Plastic White Bead Sorting Tray Triangular Plate and 1 Pencil Sharpener
42. [All Beauty] Setgnur Waterproof Nail Art Table Mat 100 Pcs Waterproof Nail Pad Protector Nail Art Mat Sheet for Home Office Nail Salon Beauty Salon (Pink)(100PCS/Roll)
43. [All Beauty] St. Patrick's Day Nail Polish Stickers Full Cover Nail Wraps Sticker Shamrocks Nail Art Decals Self-Adhesive Nail Strip Irish Green Luck Design Nail Art Supplies Decorations with Nail File 12 Sheets
44. [All Beauty] Sunflowers Nail Art Decorations Flowers Nail Art Supplies Yellow Daisy Flowers Charms Butterfly Bee Nail Design Nail Art Stickers Decals Foils Wraps Tattoo for Women Nail Accessories 1 Big Sheet
45. [All Beauty] Tattify Christmas Winter Nail Wraps - Let it Snow (Set of 22)
46. [All Beauty] Tattify Mouth Nail Wraps - Vampire's Night Out (Set of 22)
47. [All Beauty] Tojwi Colorful Stainless Steel Rhinestone Nose Studs, 20 Pieces
48. [All Beauty] Umillars 12 Boxes Mixed Element Nail Art Rhinestones Decorations Set,3D Nail Studs Crystals Gems DIY Design Manicure Diamonds Jewels Accessories
49. [All Beauty] WOKOTO 4Pcs Metal Nail Art Studs Charms And Rhinestones Kit With Tweezers And Picker Pencil Rose Gold Hollow Mix-Shapes Nail Studs Rivet Mix-Color Rhinestones Flatback Decoration Kit
50. [All Beauty] lorelo 80 pieces Toenail Corrector Stickers, Toenail Treatment Tape Elastic Patch Sticker Corrector Pedicure Tools Fingernail Toe Nail Care Protects Toe Nail

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 9
Cluster size: 457

Representative product titles:
1. [All Beauty] (BX) m9 Odor Eliminator Spray
2. [All Beauty] 16 oz, Dark Brown - Bargz Perfume - Kush Type Body Oil Scented Fragrance
3. [All Beauty] 3 PIECE AVON HAIKU KYOTO FLOWER GIFT SET
4. [All Beauty] 3-Pack Rose Vanilla Natural Deodorant Stick, 2.65 oz
5. [All Beauty] Annick Goutal Eau d'Hadrien 0.05 oz EDT Sample Vial
6. [All Beauty] Argan Heat Protecting Spray 2 Oz.
7. [All Beauty] Aromatherapy Essential Oil Diffuser, 500ml Super Quiet Aroma Humidifier, Water Auto off, Sleep Night Light for Home Office
8. [All Beauty] Attraction Room & Body Spray 4 oz | Handmade with Infused Herbal Oil | Love, Money & Prosperity Rituals | Hoodoo, Voodoo, Wicca, Pagan
9. [All Beauty] Avon Black Suede SPORT 3.4 Fl Oz Eau De Toilette Spray LOT OF 2 sealed sold by The Glam Shop
10. [All Beauty] Bath & Body Works - Buttercups & Berry Bellini - 2 pc Bundle - Fine Fragrance Mist and Ultimate Hydration Body Cream - 2022
11. [All Beauty] Bath & Body Works Warm Vanilla Sugar Very Merry Wrapped Gift Set - Body Cream & Fragrance Mist
12. [All Beauty] Bath and Body Works Coconut Pineapple Body Cream Fine Fragrance Mist Set
13. [All Beauty] Bottega Veneta Eau De Velours for Women Eau De Parfum 2.5 Ounce SPR
14. [All Beauty] Britney Spears Rocker Femme Fantasy Eau de Parfum 1.7oz (50ml) Spray
15. [All Beauty] CLINIQUE AROMATICS ELIXIR EAU DE PERFUME 100ML VAPO. 75ML + BODY MILK + ELIXIR 6ML
16. [All Beauty] Clubman Supreme Non-Aerosol Styling & Grooming Spray 8 oz (Pack of 10)
17. [All Beauty] Commodity Moss Eau De Parfum Spray Unisex 3.4 oz / 100 ml Brand New Item In Box Sealed
18. [All Beauty] Degree Deod Inv Sld Clean Size 2.7z Degree Ultra Dry Clean Invisible Stick Deodorant - Pack of 2
19. [All Beauty] Degree Deodorant 3.8 Ounce Mens Dry Spray Overtime (113ml) (2 Pack)
20. [All Beauty] Desodorante Yodora Crema X 60g Producto de Colombia
21. [All Beauty] Dove Advanced Care Anti-Perspirant Deodorant, Revive 2.6 oz (4 Pack)
22. [All Beauty] Dove Men + Care Dry Spray Antiperspirant, Sensitive Shield 3.80 oz (Pack of 8)
23. [All Beauty] Estee Lauder 'Sensuous Sensual' Duo
24. [All Beauty] Feulover-Bitter-Apple-Spray-for-Dog-to-Stop-Chewing, No Chew Spray for Dogs, Pet Corrector Spray for Dogs&Cats, Stop Chewing Licking and Biting, Nontoxic
25. [All Beauty] Fictions Perfume Spray for Women - London. She Knew He Was Forever - Fresh, Light, Feminine Daytime Fragrance - Travel Sized Purse Spray - 0.5 oz 15 ml
26. [All Beauty] GK 1 Perfume for Men Eau de Toilette Spray With A Deluxe Suede Pouch, Great Gift, Purity, Daytime and Casual Use, for all Skin Types, a Classic Bottle, 3.4 Fluid Ounce
27. [All Beauty] Giorgio Armani Si Passione Women's Eau De Parfum 3.4 oz 4 Piece Gift Set
28. [All Beauty] I.D. - L'BEL - Eau de Toilette Colonia 100 ml e (3.4 fl.oz) UNISEX
29. [All Beauty] LOCA LOCA Perfume for Women - 2.7 Fl Oz
30. [All Beauty] Label.m Hair Perfume New! 50/ml
31. [All Beauty] MARC JACOBS by Marc Jacobs Gift Set -- 3.4 oz Eau De Parfum Spray + 5.1 oz Body Lotion + .34 oz EDP Roller Ball
32. [All Beauty] Musk Mood - Eau De Parfum Spray (100 ml - 3.4Fl oz) by Lattafa
33. [All Beauty] NEST Fragrances - CITRINE (1.7fl oz / 50 ml)
34. [All Beauty] Narcisse Perfume By Chloe-3.4 oz Eau De Toilette Spray (Tester)
35. [All Beauty] Organic Aromatherapy Essential Oil - 100% Pure Essential Oil for Hair, Skin and Diffuser Best Therapeutic Grade Essential Oil (10mL) (Tangerine)
36. [All Beauty] Our Time
37. [All Beauty] Perspirex Strong 20mL - 0.67oz. by Perspirex Strong
38. [All Beauty] ROYCE BLUE EAU DE PARFUM 3.4 FL OZ
39. [All Beauty] Rue 21 Perfume For Women Crystalline Moonstone 3.4oz Eau De Parfum rue21
40. [All Beauty] Rue21 Cologne For Men Neon Universe 2.5 Ounce Brand New In Box Rue 21
41. [All Beauty] Secret Clinical Strength Soft Solid Sensitive Unscented Deodorant, 1.6 oz (Pack of 5)
42. [All Beauty] Secret Outlast Antiperspirant & Deodorant Invisible Solid, Unscented 2.6 oz (Pack of 10)
43. [All Beauty] Sex In The City Kiss by Instyle Parfums Eau De Parfum Spray 3.4 oz
44. [All Beauty] Shakira Perfumes - Dance for Women - Long Lasting - Femenine, Charming and Modern Perfume - Fruity Floral Notes - Ideal for Day Wear - 1.7 Fl Oz
45. [All Beauty] Skymore Aromatherapy Diffusers Cool Mist Humidifier, Essential Oil Diffuser with 7 Color LED Lights Changing for Office, Home and Bedroom
46. [All Beauty] Thierry Mugler Angle Eau De Parfum 1.7 fl oz Women's- - 1.7 oz - 008 Black
47. [All Beauty] Willowbrook Fresh Scents Scented Sachet - Magnolia
48. [All Beauty] Yves Rocher Muguet en Fleurs Lily of the Valley Eau de Toilette, 100 ml. THIS EDITION IS NOT AVAILABLE IN USA. Imported from France.
49. [All Beauty] Yves Saint Laurent Black Opium 1.6 Oz Eau de Parfum Spray - Wild Edition Bottle Design
50. [All Beauty] ZARA APPLEJUICE EDT 30 ML (1.0 FL. OZ). - FRESH FLORAL EAU DE TOILETTE - FEMININE, DELICATE AND BRIGHT FRAGRANCE - Eau De Toilette

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 10
Cluster size: 719

Representative product titles:
1. [All Beauty] Bee Naturals Best Skin Cream Bar - Solid Form Hand Lotion - Purse Size Travel Container - Smooth, Soothe and Soften Your Hands. (Lavender)
2. [All Beauty] Bello 99% 0 Water Baby Wipes 15PK, 900ct
3. [All Beauty] Calgon Ultra Moisturizing Bath Beads 30 Oz (Ocean Breeze, Pack of 2) by Calgon
4. [All Beauty] Candy Wishes Holiday Lotion
5. [All Beauty] Clear Natural Beauty Soap (African Black Soap, 4 Pack)
6. [All Beauty] Coconut Vanilla Aromatherapy Body Oil - 8oz - 100% Pure & Natural
7. [Premium Beauty] Cuccio Naturale Spa Essential Kit - Infused With Essential Oils That Dissolve Quickly - Leaves Skin Feeling Soft And Polished All Day - Healthy, Glowing Effect - Milk And Honey - 2 Pc
8. [All Beauty] Dove Men Plus Care Everyday Gift Pack, Clean Comfort
9. [All Beauty] Epil-Vite/Hair Away - Satin Sugar Wax, Enriched with Honey and Cocoa for Smooth Application, 600 grams
10. [All Beauty] Fresh Balls The Solution For Men - 5 oz
11. [All Beauty] Gelo Refill Plant Based Essential Oil Hand Liquid Soap (10 oz.) Choose From: Bottle, Refill Pods or Both (Sea Mist, Mineral & Freesia, Pods Only) + 1 Complimentary Assorted Car Jar
12. [All Beauty] Greenwich Bay CUCUMBER OLIVE OIL Spa Soap, Enriched with Cucumber Oil, Virgin Olive Oil & Shea Butter. No Parabens, No Sulfates 6.35 Oz. (3 Pack)
13. [All Beauty] Greenwich Bay Mini Soap Sampler Set, Rich in Shea Butter, African Violet, Passion Flower, Zinnia, Orchid, Lavender, Rosewater, No Parabens, No Sulfates 6 x 1.9 oz.(Flower)
14. [All Beauty] GuruNanda Beauty Oils - Pure and Natural (Almond Oil)
15. [All Beauty] H2O ECO Amenities Spa Sachet Individually Wrapped 1 ounce Cleaning Soap, 300 Bars per Case
16. [All Beauty] HENIUY 3 Pack Bar Soap for Women, 6.35oz Each Natural Soap Bar with Bubble Foam Net - Handmade Clean Moisture Bath Soap for Hand Face Body Skin Care Soap Gift Sets
17. [All Beauty] Happy Bath Body Wash 500g (1 pack) (Cherry Blossom)
18. [All Beauty] Hard Wax Beans by Grace Lane | Hair Removal Hot Paraffin Waxing 1 Pound (Karitene)
19. [All Beauty] Hawaiian Tropic Tropic Island Sport Lotion, SPF 30 Light Tropical Scent 10.8oz (light tropical)
20. [All Beauty] Hempz Pomegranate Herbal Body Moisturizer - 21oz
21. [All Beauty] Hesh Ancient Formulae Shikakai Hair Soap (75 Grams) X Pack of 3
22. [All Beauty] Hibiclens Antiseptic/Antimicrobial Skin Liquid Soap, 32 Fluid Ounce by Hibiclens
23. [All Beauty] J.R. Watkins Liquid Hand Soap, Desert Rose, 11 Ounces
24. [All Beauty] K. Hall Designs Milk Hand & Body Cream 3.4oz
25. [All Beauty] Kart Natural Medicure Pomegranate Soap 100 ml / 3.4 fl.oz
26. [All Beauty] La Florentina, Bellosguardo Collection:"Agrumi di Boboli" - Hand Wash Liquid Soap, Citrus Scent 16.5 fl.oz. (500 ml). Italian Import.
27. [All Beauty] Lavender Oatmeal Soap Gift Set for Men and Women. Vegan Soap with Therapeutic Grade Essential Oil, Organic Oatmeal, Skin-Loving Shea Butter. Set of 3 Bars in Gift Box.
28. [All Beauty] Michel Design Works Large Bath Soap Bar - Confetti
29. [All Beauty] Mongo Kiss® Coconut Organic Lip Balm, 0.25 oz. - 3 Pack!
30. [All Beauty] Olay Ultra Moisture Moisturizing Body Wash, Vanilla Winter Retreat, 23.6 oz
31. [All Beauty] Organic Calendula Baby Massage Oil - Natural Skin Moisturizer with Vitamin E, Sunflower and Lavender Essential Oils - Infant Rash, Cradle Cap, and Eczema Treatment - Safe and Chemical Free (8oz)
32. [All Beauty] Organic Snail Gel Hydro Elixir
33. [All Beauty] Perlier Olivarium Ultra Rich Body Butter with Olive Oil Large 6.7 fl oz
34. [All Beauty] Raw Sugar Watermelon + Fresh Mint Moisture Loving Lip Balm and Lip Scrub Gift Set, Pack of 1
35. [All Beauty] SUNAROMA Oatmeal Soap with Vitamin E (4.25 oz) - 100% Vegetable Based Soap - Great for Sensitive or Eczema Prone Skin - Made in the USA, Sulfate Free
36. [All Beauty] Sculpt 3X Body Tight Caffeine Tightening Lotion 32oz
37. [All Beauty] Senzokan - Famous Traditional Beauty Herbal Soap - Deeply Cleanses and Gentle Care your Skin with the Medical Plants (1 x 100 gr)
38. [All Beauty] Simple Pleasures Scented Hand Cream Collection Gift Set Of 5 Mini Hand Lotions with Sweet Winter Seasonal Holiday Fragrances For Home Or Travel Use In A Giftable Red Window Box by Tri-Coastal Design
39. [All Beauty] Sothys Soothing Melting Fluid 5.07oz Pro
40. [All Beauty] Spanature Lavender Hand & Body Lotion Travel Size Selection 4 Pack, Relaxing and Revitalizing Moisturizer for Rough and Dry Skin, Nourishing and Gentle for All Skin Types, Made In Korea - 75 ml/2.53oz
41. [All Beauty] Swanson Certified Organic Carob Powder 1 lb (454 g) Pwdr
42. [All Beauty] Sweet Baby Shampoo 16oz., Sulfate Free, No Parabens, Phthalates, Dyes, Endocrine Disruptors, SLS Free, Vegan, Natural (Tropical Baby 16 oz)
43. [All Beauty] The Woods Beard Balm - Pine and Cedarwood - Essential Oil Scented Beard Conditioner Beard Balm by The 2Bits Man
44. [All Beauty] Vaseline Body Lotion, Aloe Fresh 400ml / 13.5oz (3 Pack)
45. [All Beauty] Venezia Soapworks Pure Vegetable Bath Soap Combo (4 Pack). iwgl
46. [All Beauty] Windrift Hill Moisturizing Goats Milk Soap (Eye Opener)
47. [All Beauty] Wit and Wisdom New York Shaving Balm and Shaving Cream Set
48. [All Beauty] Zen Dairy Applejack Goat Milk Soap
49. [All Beauty] Zylast Antiseptic Foaming Soap (8.25 oz.)
50. [All Beauty] tamarinda Bulk Glycerin Soap, 3 pound loaf - Tea rose

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 11
Cluster size: 659

Representative product titles:
1. [All Beauty] 2 Pack Grooming Comb for Dogs and Cats Eye Stain Remover Combs for Removing Matted Fur, Knots & Tangles, Long Metal Teeth Flea Comb and Pet Lice Comb Metal Cat Comb
2. [All Beauty] 2 Pcs Silicone Bath Body Back Brush+Silicone Shower Brush with Soap Dispenser,Ultra Soft Exfoliating Silicone Body Scrubber, Easy to Clean, Lathers Well, Eco Friendly, Long Lasting
3. [All Beauty] 5 In 1 EARTH REHAB Bamboo Bathroom Bundle, Bamboo Razor With 5 Razor Blade Refills | Bamboo Toothbrush with Bamboo Case | 100 Bamboo Cotton Swabs
4. [All Beauty] 5 Pieces Detangling Brush Set, Includes Detangler Brush, Edge Brush, Rat Tail Comb with Stainless Steel, Wide and Fine Teeth Comb for Braids Hair Salon Home Supplies Afro American Hair Types
5. [All Beauty] 9 Pieces Detangling Brush Set Includes Hair Detangler Hair Edge Brush Wide Tooth Tail Comb for Wet Dry Long Thick Curly Hair, Smooth Comb Grooming
6. [All Beauty] AIMIKE Scalp Massager Shampoo Brush, Soft Silicone Scalp Brush Hair Scrubber, Hair Washing Scalp Exfoliator Brush for Dandruff, Head Scrubber for Thick Curly Wet Dry Hair of Women Men Kids, Green
7. [All Beauty] ANNIE Jumbo Detangler Comb (Model:121)
8. [All Beauty] AZDENT Textured Disposable Finger Teeth Wipes Brush Ups Dental Clean Pre/Post Whitening
9. [All Beauty] AngLink Eyebrow Hair Remover USB Rechargeable Painless Portable Precision Electric Eyebrow Trimmer Removal Razor Tool for Women (Red)
10. [All Beauty] BIC Hybrid Advance 3 Disposable/System Shaver for Men, 6 Count
11. [All Beauty] Barber Beauty Hair Cleopatra 450 7" All Purpose Combs (12 Pack) 12 x SB-C450-BLK
12. [All Beauty] Barber Cape and Neck Duster Brush Comb Set, Waterproof Hair Cutting Cape Professional Hairdresser Cape Salon Supplies Tool Set for Hair Treatment/Cutting/Coloring/Perming(55x63Inch)
13. [All Beauty] Beard & Hair Roller Black w/Green 540 Stainless Steel Microneedling Derma Roller MOOKARDILANE Face Home Use
14. [All Beauty] Beard Care Kit, 7PCS All-in-one Natural Material Beard Growth Kit Beard Brush+Beard Oil+Beard Balm+Wood Comb+Beard Catcher Apron+Beard Comb+Storage Bag Great Gift for Men
15. [All Beauty] Bicrops Professional Haircutting Shears Kit, Stainless Steel Beard Hairdressing Scissors Set, Regular Hair Shear, Thinning Scissor, Leather Case. Home Hair Salon For Men And Women
16. [All Beauty] Bikini Trimmer for women Raymeefa Upgraded Rechargable 3 in 1 Painless Electric Shaver, Hair Removal for face Legs Chin Lips Neck Armpit Bikini-line, Portable, Waterproof
17. [All Beauty] Blackhead Vacuum Removal Pore Remover Cleanser, Electric Vacuum Pore Extractor Blackhead Remover USB Rechargeable/Effective 3 suction levels/6 Replaceable Suction Heads/LED Display
18. [All Beauty] Chicago Comb Model 1 Stainless Steel + Horween Olive Shell Cordovan Sheath, Made in USA, Smooth, Durable, Anti-Static, 5.5 in. (14 cm) Long, Medium Tines, Ultimate Daily Use Comb, Gift Set
19. [All Beauty] Cordless Water Dental Flosser,Portable Dental Oral Irrigator Teeth Cleaner ,Portable Oral Irrigator for Deep Teeth/ Braces Cleaning ,Chargeable IPX7 Waterproof for Home Travel (White)
20. [All Beauty] Creative Hair Brushes CP-WL Birchwood Paddle
21. [All Beauty] DOOPER Bikini Trimmer,Ladies Electric Razor,Facial Hair Remover,Nose Ear Trimmer,Bikini Shaver,Women Electric Shaver for Face,Nose,Bikini Line,Leg,Body Hair Removal Kit(red)
22. [All Beauty] Dog And Cat Deshedding Tool - Helps Stop And Reduce Shedding For Dogs And Cats - Brush Comes With Large & Small Changeable Blade/Comb - Deshedder Brushes Provide Shed Relief For Pet
23. [All Beauty] Dog Brush and Cat Brush Combo Gel Dog Grooming Tool for your Pet
24. [All Beauty] Electric Hair Brush Straightener, Portable Electric Ionic Hairbrush Takeout Mini Hair Brush Comb Massage for Women (pink)
25. [All Beauty] Emjoi eRase e60-60 Tweezer Head Epilator
26. [All Beauty] Firefly Kids Flossers 30 Count, Pack of 3
27. [All Beauty] Hair Cutting Combs Barber Hair Comb Carbon Fiber Pet Comb Heat Resistant Cutting Comb Long Hair Comb Styling Comb Size Marked Doubtless Bay (4pcs set)
28. [All Beauty] Hair Scalp Massager Brush, 4PCS Silicone Brush, Wet And Dry Hair Scalp Brush With Soft Rubber Perfect for Men, Women
29. [All Beauty] Hair Shampoo Brush & Body Brush 2-in-1 Kit, ALLYAG Soft Silicone Hair Scalp Massager and Body Scrubber for Exfoliate and Improve Blood Circulation, Used in Wet & Dry, Fit for Women, Men, Kids, Pets
30. [All Beauty] Hair Straightener Brush,Hair Straightening Brush,Hair Comb,Adjustable Hair Straightener Comb
31. [All Beauty] Hair Thinning Scissors Cutting Teeth Shears, 6.5 Inches Stainless Hair Cutting Scissors Teeth Edge Hair Cutting Texturizing Shears for Women, Men, Barber, Salon, Home
32. [All Beauty] Henry Cavendish Himalaya Shaving Kit with - Shaving Soap, Long Lasting 3.8 oz Puck Refill, plus Stainless Steel Shaving Soap Bowl, plus Gentleman's 100% Pure Badger Hair Shaving Brush.
33. [All Beauty] Krest 8 Inches Barber Styling Hair comb. Clipper Cutting Comb. Made of Nitrile Rubber.
34. [All Beauty] Laxcare Water Flosser, Cordless Teeth Cleaner Rechargeable Portable Oral Irrigator with 3 Modes, IPX7 Waterproof Dental Flosser with 2 Replaceable Tips,Detachable Water Tank for Home Travel, Cyan
35. [All Beauty] Life-Q SH70 Shaver Heads Replacement, 3Pcs Electric Shaver Head Replacement Blades Cutter Compatible with Norelco 7000 Series Razor
36. [All Beauty] Mini Folding Teasinging Brush for Creating Volume,Traval Portable Rat tail Comb for Smoothing,Backcombing,Styling and Slicking Back Fine Thin Hair, Hair Salon/Home Use - Purple
37. [All Beauty] New Uppercut Deluxe Men's Black Comb Black
38. [All Beauty] Norelco HS800 Lotion Refill
39. [All Beauty] Oral-B Professional Care Smart Series 5000 Rechargeable Toothbrush with Crest 3D White Professional Effects Whitestrips
40. [All Beauty] Petco Cushion Pin Cat Brush
41. [All Beauty] Philips Norelco 7110 Cordless Rechargeable Shaver
42. [All Beauty] Replacement Brush Heads Compatible with Braun Oral B Electric Toothbrush 16 Count
43. [All Beauty] Sandalwood Hair Comb, 100% Handmade Wooden Detangling Wide Tooth Comb with Natural Aroma
44. [All Beauty] Satin Smooth Natural Muslin Waxing Cloth Roll for Hair Removal, 3.5 in x 40 yards
45. [All Beauty] Schick Bare By Schick Dermaplaning Tool With 2 Dermaplaning Razors and 1 Cleaning Brush, 2 Count
46. [All Beauty] Shaving Razor Replacement Head for Philips Norelco SH50/52 S5000 S5010 S5380 S5570 S5571 S5420 Shaving Head Cutter
47. [All Beauty] Silicone Back Scrubber for Shower, Lengthen Exfoliating Double Sided Bath Body Brush Towel for Taking a Shower Deep Clean and Relax Your Body-Blue
48. [All Beauty] Sprmal Eco-Friendly Natural Bamboo Charcoal Toothbrush-Pack of 5,Individually Numbered,Zero Plastic Packaging,Biodegradable Organic Bamboo Handle and BPA Free Soft Nylon Bristles for Sensitive Gums
49. [All Beauty] Waterproof Barber Cape Protector Haircut Cloth Apron Neck Duster Brush Barber Supplies Tool Set
50. [All Beauty] ZRKFSR Pet Grooming Tool，2 Sided Undercoat Rake for Dogs &Cats，Deshedding Tool Great for Short to Long Hair Cats &Large Small Dogs，Safe and Effective Dematting Comb for Mats &Tangles Removing (Blue)

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 12
Cluster size: 504

Representative product titles:
1. [All Beauty] 100% Remy Human Hair Silk Base Top Hairpieces Replacement Clip in Topper For Women Crown Top Piece Short 10''/10inch #27 Dark Blonde 20g
2. [All Beauty] 1017 Pcs Topsy Hair Tool Tail Hair Braiding Tools Include French Centipede Braiders Twist DIY Hair Styling Kit Tool Colorful Mini Rubber Elastic Hair Ties Bands Set Hair Tail Ponytail Updo Maker Comb
3. [All Beauty] 3 Pieces Double Layer Twist Plait Headband Hair Tools, Double Bangs Hairstyle Hairpin Double Layer Clips and Multi-Layer Hollow Woven Headband Double Bangs for Hair Accessories (Black)
4. [All Beauty] 4 Pcs Large hair Claw Clips for Thick Thin Curly neutral Wavy straight Hair 4.3 Inches for Girls Women 90's Strong Jaw hold Non Slip Matte (1)
5. [All Beauty] 4 Pcs Retro Gold Color Butterfly Mini Side Combs DIY Bridal Hair Accessories Decorative Metal Hair Combs, 1.6 Inches
6. [All Beauty] 4 Pieces Hair Bun Maker，Inclde 2 Large Donut Hair Buns 2 Medium Bun Makers…
7. [All Beauty] 4 pcs NEW VINTAGE LARGE COMB BANANA CLIP HAIR RISER CLAW(1Brown-1Black-1White-1Clear).
8. [All Beauty] 50 Pcs Alligator Curl Clips, Bantoye 2.2 Inch Single Prong Clips Double Hole Clips Hair Accessories for Hair Styling, Hair Coloring, Silver
9. [All Beauty] 6 Pack Instant Hair Volumizing Clips For All Hair Types Hair Root Volume Clip Hair Curler Clip Volumizing Hair Root Clip DIY Natural Curler Clamps Rollers Fluffy Hair Roots Styling Tool (Black 6 pcs)
10. [All Beauty] 6 Pieces Rhinestone Double Flower Hair Clips Non-slip Comb Rhinestone Hairpins Pearls Design Women Hair Dovetail Clips Rhinestone Floral Hair Clips for Women Girls (Retro Color)
11. [All Beauty] 72 Pieces Weaving C-curve Needle (Large) #70010
12. [All Beauty] 8 PCS Womens Korean Fashion Crystal Rhinestone Barrette Hairpin Hair Clip Accessories (Random Color)
13. [All Beauty] 9 Pack Acrylic Hair Clips for Women,Alligator Hair Clips for Styling Small Hair Clips for Hair Barrettes for Women Alligator Clips for Hair Accessories for Women
14. [All Beauty] ANBALA 16 Pack Velvet Hair Scrunchies Soft Velvet Scrunchy Bobbles Elastic Hair Bands Ties Hair Accessories for Women, 16 Pack
15. [All Beauty] AOPRIE 18pcs Hair Pins for Women Girl Bride Crystal Rhinestone Starfish Blue Jewelry Bag Starfish Rhinestone Starfish Wedding,Party DIY
16. [All Beauty] Agate Gemstone Arrow Head Dreadlock Bead Loc Jewelry Braiding Hair Accessory Natural Stone Decorations
17. [All Beauty] Ankha Hair Claw Clips Medium for Women Girls Hair Clips No Slip Great for Thick Thin Hair
18. [All Beauty] Beauty Wig World 20 Inch Curly Synthetic Clip in Claw Ponytail Hair Extension Synthetic Hairpiece Jaw Clip Claw in-14/613
19. [All Beauty] Beautywin 160 Pieces DIY Braid Rings Dreadlocks Metal Cuffs Beads Multiple Style for Festival Party Hair Decoration Accessory
20. [All Beauty] Braided Hair Clips for Women Girls, Sparkling Crystal Stone Braided Hair Clips Barrette with 3 Small Clips, Triple Hair Clips with Rhinestones for Sectioning,8PCS (8pcs-Mix)
21. [All Beauty] Briskaari U Shape Hair Fork Gold Updo Hair Sticks Bowknot Prong Bun Hair Pins Clips Grips Hair Styling Tool Hair Accessory Wedding Daily Party Gift for Women and Girls (Gold)
22. [All Beauty] Brown Elastic Hair Ties No-Metal Ouchless Ponytail Holders 100 Count 3MM
23. [All Beauty] Diane Bobby Pins, Black, 2", 300 Count
24. [All Beauty] GIMME Glitter Garden Clips 8pc
25. [All Beauty] Goody Mesh Rollers & Pins 8 Pieces Set
26. [All Beauty] Goody Simple Styles Spin Pin Dark Hair
27. [All Beauty] Green Foam Plumeria Flower Hair Clips - Set of Three
28. [All Beauty] HAYLEY Clip On Hairpiece by Mona Lisa - 130 Copper Red
29. [All Beauty] Hair Bun Dish Chignon Curly Clip in Grey
30. [All Beauty] Hair Claw Clips,Hair Banana Barrettes for Women Girls Celluloid French Butterfly Jaw Clips Tortoise Shell Grip Pin Teeth Clamp Leopard print Stylish Hair Accessories for Thick or Thin Hair
31. [All Beauty] Hair Scrunchies Large, Hair Bow Chiffon Ponytail Holder Elastic Hair Bands Hair Ties Ropes for Women or Girls Hair Accessories Pack 4
32. [All Beauty] Halloween Skull Hair Clips Butterfly Halloween Skeleton Butterfly Gothic Hairpin BHWH02 (3 Pcs-Set)
33. [All Beauty] Halo Hair Extensions Invisible Elastic Wire Hairpieces No clips, No glue 8006#99J
34. [All Beauty] Hapdoo Minimalist Dainty Hairpin 15pcs Geometric Hair Clip Clamps for Women Girls, Starfish, Circle, Triangle, Moon, Leaf hair barrettes
35. [All Beauty] Hraindrop 36 pcs/18 pairs Pet Dog Hair Bows With Rubber Bands - Bowknot Bows Dog Hair Accessories with Varies Pattern
36. [All Beauty] MLBSN 2021 New 36 Pcs Rhinestone Easy Bun Maker, Donut Bun Maker, Rhinestone Hair Band Accessory, Easy Hairstyle Tool DIY Hair Styling Tool for Women Girls (3 Pcs-A)
37. [All Beauty] OIIKI 6PCS Hair Clips
38. [All Beauty] OPCC 50pcs Black Spiral Hair Pin Clip Bun Stick Pick for DIY Hair Style / Sleek and Compact Alloy Construction, Designed to Fit for All Hair Type, easy to use for your perfect bun hair style
39. [All Beauty] OWIIZI Hair Deft Bun Maker, Magic Headband Clip for Hair Bun Hair bands French Twist Hair Tool Hair elastics Hair Accessories for Women
40. [All Beauty] Ribbon Hair Ties No Tangle No Crease Tie Dye Multi Color 30 Pack
41. [All Beauty] Sequin Sparkling Pom Poms Ball Hair Bows Fluffy Elastic Hair bands Buns Srunchies girls Headpiece Costume Accessories: M22 (PomPom-Pink1)
42. [All Beauty] Set of 6 Trillium Flower Rhinestone Crystal Hair Pins H010
43. [All Beauty] SuPoo 10 PCS Pearl Hair Clips Leopard Print Acrylic Resin Hair Barrettes Fashion Geometric Crystal Rhinestone Alligator Hair Clip Decorative Hairpins Bobby Pins Hair Accessories for Women
44. [All Beauty] TOBATOBA 18pcs Hair Scrunchies Flowers Elastic Hair Bands Scrunchy Hair Ties Ropes Scrunchie Hair Scrunchies Bunny Ears Hair Bow Chiffon Ponytail Holder for Women
45. [All Beauty] TecUnite 170 Pieces Aluminum Dreadlocks Beads Metal Cuffs Hair Wraps Natural Painted Wood Beads Hair Braiding Beads Jewelry Hair Decoration Accessories with Storage Box
46. [All Beauty] Women Hair Claw Clips Medium Banana Clips Blossom Petal Hair Barrettes for Women and Girls Hair Accessories for Thick Hair (Pink 2 Pack)
47. [All Beauty] Yeshan Vintage Jewelry Rhinestone and Crystal beaded Butterfly Design Hair Barrette Clip for Beauty Tool,White
48. [All Beauty] Yeshan Women Rhinestone Crystal beaded Flower Pattern Hair Barrettes Clips,Golden
49. [All Beauty] Zodiac Hair Pins Rhinestones Paved Constellation Letter Hair Clips Bobby Pins Wedding Crystal Bling Bridal Styling Barrette (Aries)
50. [All Beauty] uxcell Lady Rhinestone Decor Light Purple Bowknot Shape Barrette Hair Clip w Snood Net

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 13
Cluster size: 873

Representative product titles:
1. [All Beauty] 100pcs Clear Disposable Plastic Shower Ear Covers Bathing Hair Dye Ear Protector Cover
2. [All Beauty] 3D Face Mask Bracket Silicone Nose Pads Lipstick Protection Stand Washable Reusable Internal Support Frame for Comfortable Face Cover Wearing (3PCs)
3. [All Beauty] 4Pcs Fashion Covering with 10Pcs PM 2.5 Activated Carbon Filter Insert Paper, Reusable Washable Cotton Mouth and Nose Cover
4. [All Beauty] Adecco LLC 2PCS Colorful Murano 3D Flower Glass Pendant Necklace Mix Color Set (green and yellow)
5. [All Beauty] Amazing Elegant Golden Earrings/Ear Studs In Butterfly Shapes Embellished With Colourful Rhinestones Gems Crystals By VAGA
6. [All Beauty] BLACK Salon Spa (USA Made) Client Gown, Kimono BLACK Silkarah + FREE YS Park Chignon Clips
7. [All Beauty] Bar5F Cotton Coil 100% Pure, 40 Feet Per Bag, White, 2 Count
8. [All Beauty] Brightdeal 8pcs Set New Black Bondage Kit Bdsm Sm Restraints
9. [All Beauty] Cheyenne Hawk Footswitch
10. [All Beauty] Color Street Made in Milan
11. [All Beauty] Cosmetic Bags Makeup Case Travel Toiletry Storage Organizer for Women by H&L (Rose)
12. [All Beauty] Designer Skin Juicy
13. [All Beauty] Dry Divas Designer Shower Cap For Women - Washable, Reusable - Large Bouffant Cap With Vintage Jeweled Brooch (Dash'n Diva)
14. [All Beauty] Ear Covers For Shower 100 Pack Clear Disposable Ear Protector Waterproof Elastic Clear Shower Water Covers Caps
15. [All Beauty] Easygluco Plus Test Strips 100 Ct
16. [All Beauty] FUMUD Gold Plated Royal Regal Blue Rhinestones Quinceanera Vintage Luxury Tiaras And Crowns Wedding Party Accessories
17. [All Beauty] FUMUD Height 2.7'' King Crown Imperial Medieval Pageant Prom Accessories Rhinestone Irises Taria Full Round Crown
18. [All Beauty] Fuller's Earth & Bentonite Combo Clay - 300 Grams
19. [All Beauty] Galaxy S9 Screen Protector [2-Pack],Cafetec [9H Hardness] [Anti-scratches] [Anti-Fingerprint] Tempered Glass Screen Protector Film for Samsung Galaxy S9.
20. [All Beauty] Goody Styling Essentials Shower Cap, 3 Count (4-Pack)
21. [All Beauty] HOYOFO Travel Makeup Bag for Women Portable Cotton Make Up Pouch with Handle Cosmetic Beauty Bag, Yellow Grid
22. [All Beauty] Hairspray Shield - Delaman 50Pcs Multifunctional Transparent Plastic Eye Face Protector Clear
23. [All Beauty] Happy Hours - Universal Car Anti Glare Sun Visor for Day and Night / 2 in 1 Anti-dazzle Shade Board Mirror Vision Goggles Clips
24. [All Beauty] Hisight Bath Shower Sponge Emoji-Pop Smiley face Plush Pillow Universe Pouf Mesh Kids Toy Brush Shower Ball, Mesh Bath and Shower Sponge,cartoon expression bath flower bath ball (3 Packs)
25. [All Beauty] Hot Sale! AMA(TM) Men Women Dial Quartz Analog Watch Bling Bling Elastic Finger Ring Watch Gifts (Gold)
26. [All Beauty] Hot Sale!Women Dress,Canserin Women's 2017 Casual Lace Sleeveless Beach Short Dress Tassel Mini Dress (M, White)
27. [All Beauty] Huaye Mavic 2 Drone PC Paddle 8743F Propellers Quick Release Folding Drone Accessories for DJI Mavic 2 Pro/Mavic 2 Zoom (Blue, 2 pairs)
28. [All Beauty] Huggies Wipes, Alcohol Free, Disney Princess, 32 ct (Pack of 16)
29. [All Beauty] It Works Fab Wrap
30. [All Beauty] JOVANA Retro Classic vintage Bronze butterfly pendant necklace chain
31. [All Beauty] Kaleidoscope Sleek Edges 2oz"Pack of 2"
32. [All Beauty] Kootek Travel Makeup Bag Portable Cosmetic Organizer Train Case with Adjustable Dividers for Cosmetics Makeup Brushes Toiletry Jewelry Digital Accessories
33. [All Beauty] LUCKY YOU FOR WOMEN BY LUCKY BRAND SET FOR WOMEN
34. [All Beauty] Legend of Zelda Million Dollar Bill (w/protector)
35. [All Beauty] Lift Nipple Cover+Double Sided Body Tape Silicone Reusable Pasties Lingerie Fashion Adhesive 4 Body Clothing.
36. [All Beauty] MASK BAND LATEX FREE-WHITE EMBO (1/4" White Embo 10yd)
37. [All Beauty] MyLadyMagic Makeup Organizer 360 Degree Rotating Cosmetic Storage Stand Box (Gold)
38. [All Beauty] Paraffin Wax Therapy/ Spa Cloth Booties- 3 Pack (Lavender/Purple)
39. [All Beauty] Pj Masks Band-Aid Bandages & Brave Blueberry Scented Hand Soap! Plus Bonus PJ Mask Character Stickers!
40. [All Beauty] Reusable Makeup Remover Pads (20 Pack) with Washable Laundry Bag +Makeup Headband Set Organic Bamboo Fiber Cotton Pads Eco-Friendly Face Pads Cotton Rounds Cleansing Wipe Cloth for All Skin Types
41. [All Beauty] Sally Hansen Salon Insta Gel Strips Troublemaker and Commander In Chic 16 Strips Each with Dimple Braclet
42. [All Beauty] Shower Caps 4 Pack Bath Caps Perfect for Women most Hair Lengths and Thicknesses - Waterproof - Double Layer, Upgraded Version (Style 2)
43. [All Beauty] Spa Massage Table Cover Oil-Resistant White
44. [All Beauty] Sun Protection Nose Patch (Beige, White)
45. [All Beauty] US Innovate Car Seat Gap Filler - Premium Full Leather Organizer with Cup Holder, Coin holder, Car Pocket Organizer for Cellphone Wallet l Driver Side l
46. [All Beauty] Unisex Dry Fit Tech Face Mouth Protective Washable Reusable Double Fabric Layers Quick Dry Sports Made In Korea (Pack of 3, Gray)
47. [All Beauty] WebDeals (R) Reading Glasses - Ultra Slim Compact Unisex, with Spring Temple. Assorted Magnification Strengths and Colors. Includes Aluminum Style Case (1.75 Black Case/Frame)
48. [All Beauty] Wrap Party 420
49. [All Beauty] ZeHuoGe Red Portable Steam Sauna Kit SPA Detox 9-Level Temperature Adjustment 6-Level Time Setting 2L Steamer Digital Display Remote 220LBS Capacity of Chair US Delivery (Red)
50. [All Beauty] itcolor Seasonal Color Swatch Palette Guide Card (Winter) Finding Right Color For Me Color Harmony Combination Fashion Hair Makeup Clothes Adviser Guide Shopping Portable Business Card Size

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 14
Cluster size: 345

Representative product titles:
1. [All Beauty] 20 Colors Nail Dip Powder Nail Kit for Starter Manicure Nail Set Includes Base Coat Activator and Top Coat, for French Nail Art No Nail Lamp Needed, Acrylic Dipping Powder Nail Set
2. [All Beauty] 7pcs Poly Gel Nail Extension Set - UV Gel Nail Extension Brush Quick Building Crystal Glue 100 with Top Coat Base Cost 6W LED Nail Lamp + Fashion 3 Colors Poly Gel Set, Portable DIY Home Gel Manicure
3. [All Beauty] 9D Cat Eye Gel Nail Polish Set, Galactic Effect Magic Gel Nail Polish Kit, 6 Colors UV LED Auroras Gel Polish
4. [All Beauty] Aushelly 6pc Nail Nutrition Oil Pen 5ML Nail Gel Cuticle Oil Nail Art Tools Makeup Accessories kit
5. [All Beauty] Avon True Color Base Coat Nail Polish
6. [All Beauty] BORN PRETTY Nail Polish Polish Pearl Transparent Shell Glimmer Shiny Shimmers Manicuring Art Varnish 5 Colors with 2 in 1 Top Base Coat
7. [All Beauty] CHERI - Gel Polish Thinner, 1 fl oz, with Dropper
8. [All Beauty] China Glaze Mediterranean Charm 70307 Nail Polish / Lacquer / Enamel
9. [All Beauty] DND Gel & Matching Polish Set #479 - Queen of Grape. Buy 5 any colors get 1 Diamond super fast drying top coat 0.5 oz Free
10. [All Beauty] Dr.'s Remedy Enriched Nail Polish, Resilient Rose, 0.5 Fluid Ounce
11. [All Beauty] Essie Wild Nudes Collection 6 Pcs Incl. 3X 0.46 fl.oz. Full Size + 3X 0.16 fl.oz. Mini Essie Shades USA Nail Salon Laquers
12. [All Beauty] FANZEST Shimmer Gel Nail Polish LED UV Soak Off Gel Polish Varnish Spring Summer Glitter Color(Green Blue)
13. [All Beauty] GND MIAMI 1 Pack of 500 pcs Wraps Aluminum Foil UV Acrylic Gel nail polish remover + Pre adhered lint free pad - Nail polish remover - Nail Polish Set - Gel Nail Kit (1PACK)
14. [All Beauty] Gel Nail Polish Crystal Summer Sweet Jelly Nail Gel Polish Kit - 8 ML 0.28oz 6 Bottles UV LED Lamp Required Soak Off Gel Polish DIY Nail Art at Home with Storage Box
15. [All Beauty] Gel Nail Polish Sets 8 Bottles - Candy Lover Selected 6 Popular Fall Colors Pink Red Brown Pure Pastel with Top Base Coat Set, UV LED Soak Off Nail Gel Polish Home Manicure Varnish Kit
16. [All Beauty] Gelaze, UP ALL NIGHT 0.5 fl oz
17. [All Beauty] Hawaii Collection Nail Polish + 10% off at checkout (Pineapples Have Peelings Too!)
18. [All Beauty] KRISNICE Color Changing Gel Nail Polish Pink Blue Purple Black Glitter Mood Thermal Temperature Chameleon Soak Off UV LED Lacquer Nail Art Varnish Set Starter Kit 6 Colors (KWB6-002-01) (KWB6-001-03)
19. [All Beauty] LeChat Dare To Wear Nail Polish - (Butterflies)
20. [All Beauty] LeChat Dare To Wear Nail Polish - (Cotton Candy)
21. [All Beauty] LeChat Nobility Nail Lacquer - 15 mL (Turquoise Sky - NBNL39)
22. [All Beauty] Lot of 2 Sensationail Color Gel Polish Kitten Heel 71602 0.25 Fl. Oz
23. [All Beauty] MASGLO Nail Polish Color - Made in Colombia - Masglo Esmalte para Uñas 13.5 ml BUSCONA
24. [All Beauty] Mac Studio Nail Lacquer/Charlotte Olympia - Good Old Days
25. [All Beauty] Matte Gel Top Coat No Wipe Gel Top and Base Coat Matte Mirror Top Coat Set 3 PCS 10 ML Soak Off UV LED Clear Nail Polish High Glossy Shiny Top Coat Matte Nail Polish Set for Home DIY and Nail Salon
26. [All Beauty] Nail Polish Base Top Coat Striping Roll Tapes Nail Art Kit Lacquer Manicure Varnish Set Soak Off UV LED FairyGlo 7ml 1005
27. [All Beauty] Nanacoco Nail Polish Too Too Dancing (6 Pieces) Salmon
28. [All Beauty] New Look berry naughty 487 New and Genuine
29. [All Beauty] New Look no place like chrome 3008 New and Genuine
30. [All Beauty] Nicole Miller Mini Nail Polish Collection- 8 Piece Glossy and Vibrant Nail Polish Set in Various Shades of Pink and Nudes, 6ml Nail Polish, Includes a Pink Folding Storage Box
31. [All Beauty] Off With Her Red! NL-A55 Nail Polish Lacquer .5oz - 1 Bottle.
32. [All Beauty] Orly Breathable Treatment + Color Nail Lacquer - State of Mind - Pick Any Color (2060013 - Peaches and Dreams)
33. [All Beauty] Orly Nail Polish Color Lacquer Set 6-Piece Collection #72
34. [All Beauty] Phoenixs 3D Paint Nail Art DIY Polish Pen Uv Gel Acrylic Tips Set Salon Beauty - Washable Glitter Pens - Classic Rainbow and Glitter Colors, Pack of 12 Pens
35. [All Beauty] Professional Nail Polish Set- Autumn Winter Caramel Series Color Soak-off Nail Gel Kit, 6 Colors 6.5 ML Classic Brown Pumpkin Caramel Cherry Red Glitter Gel Nail Polish Set, Soak-off Nail Polish Starter Set with Top Coat & Base Coat for DIY at Home
36. [All Beauty] Pure Ice Nail Polish 800 Mint Dream
37. [All Beauty] ROSEGIN 23 Pcs Gel Nail Polish Set with Glossy and Matte Top and Base Coat Soak Off Gel Polish Colors Red Black Nude Glitter Long Lasting Nail Gel Polish
38. [All Beauty] Revel Nail Dip Powder | for Manicures | Nail Polish Alternative | Non-Toxic & Odor-Free | Crack & Chip Resistant | Can Last Up to 8 Weeks | 1oz Jar | Mood Changing | Whirlpool
39. [All Beauty] Revel Nail Dip Powder | for Manicures | Nail Polish Alternative | Non-Toxic & Odor-Free | Crack & Chip Resistant | Can Last Up to 8 Weeks | 2 oz Jar | Sun Colors | (Sun Island, 2oz)
40. [All Beauty] Revel Nail Dip Powder | for Manicures | Nail Polish Alternative | Non-Toxic, Odor-Free | Crack & Chip Resistant | Vegan, Cruelty-Free | Can Last Up to 8 Weeks | 0.5 oz Jar | Mood Changing (Draco)
41. [All Beauty] Sundays Non-Toxic Nail Polish, Glossy Shine Finish. No.21: Purple Grape, Long Lasting, Vegan & Cruelty-Free, 1.7 oz
42. [All Beauty] Trind Nail Revive Natural - Nail Strengthener with no Formaldehyde .3 fl oz
43. [All Beauty] Trust Fund Beauty Le Vernis Mermaid Vibes 15 ml/0.50 fl oz
44. [All Beauty] U-Shinein Solid Nail Extension Gel, 22 PCS Nail Art Glitter DIY Kit, Solid Nail Sculpture Hard Gel, Nail Builder Gel With UV Lamp, Top Coat Base Coat, Nail Forms And Nail Files In Nail Supplies Set
45. [All Beauty] Velvet MATTE Top Gel, Gummy Jelly LED/UV Gel, Shine E Top Coat Combo Set
46. [All Beauty] Vrenmol Gel Nail Polish Set 12pcs Blue Soak off UV LED Nail Polish Nail Lacquers Nail Art Manicure Kit
47. [All Beauty] Zeva Top Coat - Speed Dry Enamel Protection - Nail Polish Top Coat - .5 Fl Oz / 15 Ml
48. [All Beauty] essie nail polish, after school boy blazer, blue black nail polish, 0.46 fl. oz, 2 count
49. [All Beauty] iLuve Long Lasting Soak Off Nail Polish with 238 Color Choices | 1 bottle with 15ml of UV Gel Polish | Taffeta Color #1359
50. [All Beauty] iLuve Long Lasting Soak Off Nail Polish with 238 Color Choices, 1 bottle with 15ml of UV Gel Polish, Whose Cider Are You On Color #1848

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 15
Cluster size: 211

Representative product titles:
1. [All Beauty] 100pc Coffin Shaped Fake Nails Tips Acrylic Ballerina False Nails Full cover Nails Tips (clear)
2. [All Beauty] 100pcs Nail Tips Shape Clear Medium Half Cover Acrylic False Nail Tips with Box (#2)
3. [All Beauty] 120 Pieces 5 Sets False Nail, Nail Art Design Press on NailsShort for Women, Full Cover Fake Nails Supplies  (short)
4. [All Beauty] 200 Pieces Transparent Nail Stand Nail Display Stand Holder Acrylic Nail Art Practice Holder Fake Nail Tips Practice Holder for Nail Salon Home Nail Accessory
5. [All Beauty] 24 Pcs Coffin Press on Nails Long, Sunjasmine Fake Nails Glue on Nails, Matte False Nails with Glue, Acrylic Nails for Women and Girls (Dark Green)
6. [All Beauty] 24 Pcs Coffin Press on Nails Short, Sunjasmine Fake Nails Glue on Nails, False Nails with Glue, Acrylic Nails for Women and Girls (Set 8)
7. [All Beauty] 24 Pcs Press on Nails Medium Length, Sunjasmine Fake Nails Almond Glue on Nails, Stiletto False Nails with Glue, Acrylic Nails for Women and Girls (Pink Swirl)
8. [All Beauty] 240 Pieces Colorful Full Cover Medium Coffin False Gel Nails 10 Colors Faux Nail Tips with Nail File, Wooden Stick, Glue and Adhesive Tabs for Women Girls
9. [All Beauty] 24pcs/Box Gourd Full Cover Manicure Tool Coffin Fake Nails Nail Tips Ballerina False Nails Wearable(05)
10. [All Beauty] 300 Pieces Extra Long Coffin Press on Nails Full Cover XXL Ballerina False Nails Cover Ballerina Nails Coffin Artificial False Nails with Storage Box for Nail Art Salon Women Girl (Clear Color)
11. [All Beauty] 432pcs Glitter Stiletto False Nails Almond Artificial Fake Nails Full Cover Fingernails Nail Tips Kit with a Crystal Nail File for Nail Art Salon DIY Decoration (Glitter)
12. [All Beauty] Acedre Coffin Press on Nails Pink False Nails Long Fake Nails Matte Faux Nails Art for Women and Girls (24 PCS)
13. [All Beauty] Barode False Nails Bling Rhinestone Gems Nail Fake Nails Elegant Wedding Birday Party Acrylic Nails for Women and Girls
14. [All Beauty] Black Nails Press On Medium, 480PCS Cosics Full Cover Coffin Ballerina & Almond Acrylic Nails Stick On Black, Solid Glossy Fake Nail Art Extension Tips with Storage Organizers for Women, Girls, Salon
15. [All Beauty] Casdre Mirror Coffin False Nails Black Long Ballerina Press On Nail Full Cover Fake Nails for Women and Girls(Pack of 24)
16. [All Beauty] Daletu Nail Clips, 10PCS Clear Nail Clips Finger Extension Fixed Clip, Quick Building Finger Builder Nail Clamps, Nails Art DIY Manicure Tool
17. [All Beauty] Fake Nails False Nail Design Pretty Nail Designs Red Fake Nails
18. [All Beauty] Fantasy Makers Long Black False Nails, Case of 12 [Misc.]
19. [All Beauty] Fdesigner Blue Fake Nails Full Cover False Nails Ombre Press on Nail Tips Cat Eye Short Acrylic Nails Square Artificial Nail Art for Women and Girls 24PCS
20. [All Beauty] Fstrend False Nails Black Red Gradient Fake Nails Full Cover Simple Party Acrylic Nails for Women and Girls
21. [All Beauty] Hilkycton 20 PCS Nail Tips Clip for Quick Building Polygel Plastic Finger Extension Forms
22. [All Beauty] IMSOHOT Oval Press on Nails Full Cover Fake Nails with Designs Long Round Rose False Nails Black Artificial Acrylic Nails for Women and Girls
23. [All Beauty] Impress Kiss ImPress Color Press-On Pedicure Toe Nails IMTS04Y9 Blue Sea (Matte Light Blue), 24 Count (Pack of 1) (85712)
24. [All Beauty] KISS Jewel Fantasy Nails Medium Length KJF04
25. [All Beauty] KISS Salon Acrylic French Nail Kit, Real Short Length 28 ea (Pack of 3)
26. [All Beauty] KISS Voguish Fantasy Nails - Leave me (FV03X)
27. [All Beauty] KISS imPRESS Limited Edition Holiday Press-On Manicure with PureFit Technology, Medium Square Press-On Nails, Style ‘Silent Night’, with Prep Pad, Mini File, Cuticle Stick, & 30 Fake Nails
28. [All Beauty] Kiss French Tip Extensions 24 Tips KFT02
29. [All Beauty] Kiss Gel Fantasy Sculpted Nails (KGFS04)
30. [All Beauty] LordHighting 240 Pieces Halloween Party/ Ball Press on False Nails with Design, 12 Sizes Medium and Long Full Cover Gloss Fake Nails for Woman and Girls
31. [All Beauty] MENGSOOD 24PCS Press on Nails Tips-Coffin Ballet Long Shiny Gold Powder Fake Manicure Full Cover Reusable Opaque Soft Gel Made Prefect & Natural Fit Medium Length for Women and Girls (Golden Line)
32. [All Beauty] MISUD Fake Toe Nails Square Geometric Triangle Silver Glitter Glossy Toe Nails Short Full Cover Vacation DIY Toenails for Women and Girls
33. [All Beauty] MUSE & Co Stick-On Gel 36 False Nails Medium Length Gloss Be Neutral Multipack (4packs)
34. [All Beauty] Magrace Blue Press on Nails Almond Medium Length 24 pcs French Fake Nails for spring Stick on Nails for Women
35. [All Beauty] Press on Nails Medium Length French Tip Rhinestones Press on Nails Blue Butterfly Fake Nails with Nail Glue Full Cover Stick on Nails False Nails with Designs for Women and Girls 24Pcs
36. [All Beauty] Press on Nails Short Square GLAMERMAID, Acrylic Fake Nails with Design Stick Glue on Nails for Women Reusable Glossy False Static Nails Art Tips Sets with 48Pcs Adhesive Tabs Nail File, Cuticle Stick, Colorful Bicolor Flower
37. [All Beauty] Professional Uv Color Builder Gel False Tips Acrylic Nail Art Set for Beauty Salon Shop, 12 24 28 36 Mixed Color Pure Solid Glitter Shiny Dust Powder Hexagon for Choose (12 Glitter Color)
38. [All Beauty] ROSALIND Long Press On Nails Gloss Fake Nails 500pcs Colorful Coffin False Nails Set 10 Colors Full Cover Acrylic Nail Tip Kit With 4pcs Glue on Nails, 2pcs Nail Sticks and 2pcs Nail Files
39. [All Beauty] Relbcy Glossy Fake Nails Red Long False Nail Stiletto Acrylic Press on Nails for Women and Girls (24 PCS)
40. [All Beauty] RikView Press on Nails Long Fake Nails Coffin Green Nails Matte Acrylic Nails with Flower Design 24PC(Green)
41. [All Beauty] SOMIER 500pcs Professional Nail Extension Guide Stickers French Nail Forms Golden Nail Art Tips for Polygel UV Acrylic Gel
42. [All Beauty] Sethexy 24Pcs Glossy Square False Nails Steelbule Gradient Glitter Silver Full Cover Art Fake Nails Tips for Women and Girls
43. [All Beauty] Sethexy Glossy Oval Medium False Nails Pink Glitter Gradient Ruby Studs Full Cover Acrylic 24Pcs Fake Nails Tips for Women and Girls
44. [All Beauty] Taktik Glossy Short Square Purple Gradient False Nails with Press on Sticker Full Coverage Acrylic Fake Nails Daily for Women and Girls 24 PCs
45. [All Beauty] Tgirls Stiletto Press on Nails Long Green Fake Nails Acrylic False Nails Matte Full Cover Nails for Women and Girls 24Pcs(Green)
46. [All Beauty] Vcedas Stiletto Nails Full Cover 240PCS Stiletto Press on Nail Tips Artificial False Nails 12 Sizes with Box for DIY Nail Salon (Clear)
47. [All Beauty] Vivid Stella 30pcs Rhombus Fake Nails Press On Acrylic Ballerina Tips Glue-On False Nails Colorful Glitter Ballerina Coffin Style
48. [All Beauty] WOKOTO 100 Pcs Fiberglass Nail Art Form Fiber Quick Building False Nail Extension Nail Acrylic Tips Manicure Accessories
49. [All Beauty] Yimart 500PCS Long Ballerina Half Cover Nail Tips Clear Coffin False Nails ABS Artificial DIY False Fake UV Gel Nail Art Tips With Box
50. [All Beauty] editTime 100pcs Super Long Glossy Fake Nails Coffin Press on Nails Ballerina Solid Color Acrylic False Nails Art Salon Ongles Fingers Nails (grey)

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 16
Cluster size: 714

Representative product titles:
1. [All Beauty] 23" Anime Cosplay Wig Big Wavy Full Bangs Wig Top Quality Synthetic Japanese Heat Resistant Fiber+Free Elastic Weaving Wig Cap - Light Blue
2. [All Beauty] 4/27 Highlight Wig Brazilian Straight Human Hair Wigs Ombre Brown Honey Blonde 13x6x1 Lace Front Wig 150% Density Highlight Glueless Lace Front Human Hair Wigs for Black Women (24 Inch, Highlight-Body Wave)
3. [All Beauty] 613 Full Lace Wig Human Hair With Baby Hair Blonde Full Lace Wig Pre Plucked Bleached Knots (18 inch, full lace wig)
4. [All Beauty] AISI HAIR Mixed Green Synthetic Short Curly Bob Wigs With Bangs Green Bob Wavy Wig for Women Synthetic Heat Resistant Bob Wigs
5. [All Beauty] AISI HAIR Short Bob Curly Bob Wig with bangs Mixed Brown Womans Natural Looking Wavy Curly Bob Wig Synthetic Heat Resistant Fiber Wig for Women (Mixed Brown)
6. [All Beauty] Anniston Hairpiece Fashion Women's Cosplay Long Curly Wavy Synthetic Hair Full Wig Costume Party Hair Scrunchies Updo Hair Bun Hair Accessories for Women - Black
7. [All Beauty] Beweig Short Curly Red Wigs Afro Wig for Black Women Fluffy Synthetic Heat Resistant Halloween Cosplay Party Full Wig
8. [All Beauty] Body Wave Lace Front Wigs Human Hair for Black Women 13x4 HD Transparent Glueless 180% Density Brazilian Virgin Human Hair Wigs Lace Frontal Wigs Pre Plucked with Baby Hair Natural Color(26 Inch Body Wave Wig)
9. [All Beauty] Burgundy Short Bob Wig with Bangs for Women14 Inch Synthetic Hair Bob Wigs Mixed Red Burgundy Short Hair Wig with Bangs for Party, Daily Use (39#)
10. [All Beauty] Chu Yao 4 Inch Short Afro Kinky Curly Wigs Synthetic Afro Wigs for Women Black synthetic fiber braided hair short curly wig Give You Beautiful Looks
11. [All Beauty] Cosplay.fm Women's Anime Cosplay Wig Wavy Long Purple
12. [All Beauty] Cupidlovehair Yellow Blonde Wave Medium 18 Inches Heat Resistant Korea Synthetic Fiber Hair Lace Front Wigs Natural
13. [All Beauty] Curly Lace Front Wig Human Hair Wigs for Black Women HD Lace Front Wigs Human Hair Pre Plucked 180% Density 4x4 Lace Closure Curly Wig Natural Black Color(26inch )
14. [All Beauty] ENTRANCED STYLES Synthetic Blonde Lace Front Wigs for Women Long Straight Wig Pre Plucked Natural Looking Wig for Daily Use Heat Resistant Fiber
15. [All Beauty] Esmee 24 Inches Long Hair Wigs for Women Ombre Color Dark Brown to Brown Synthetic Curly Hair Wig Middle Parting
16. [All Beauty] FASHION PLUS 10A Lace Front Human Hair Wigs for Women Pre Plucked Hairline 150% Denisty Brazilian Body Wave Lace Front Wigs with Baby Hair Natural Color (14 inch, 13x4 Lace Front Wig)
17. [All Beauty] FLIRTY (OT30) - FreeTress Equal Synthetic Invisible Part Full Wig
18. [All Beauty] HANNE 14" Bob Wig with Bangs Shoulder Length Yaki Srtaight Bobo Wig Heat Resistant Synthetic Hair Wigs for Women (2/30)
19. [All Beauty] Haha Ombre Water Wave Human Hair Wigs 1b/30 Ombre Brown Curly Closure Wig for Black Women Human Hair 4x4 Lace Front Wig Pre Plucked 20 Inch
20. [All Beauty] Halloween Party Online Poison Ivy Wig, Brown Adult HW-1662A
21. [All Beauty] Kamo 28" Wig Long Heat Resistant Big Wavy Hair Cosplay Wig
22. [All Beauty] LUMIERE Hair 8 inch Short Straight Bob Wig Human Hair Lace Closure Wig Brazilian Virgin Hair Straight Bob Wig for Black Women Straight Human Hair Bob Wig 4X4 Lace Closure with Baby Hair Pre Plucked
23. [All Beauty] Lace Front Wig Human Hair Straight Wigs for Black Women, 4x4 Brazilian Virgin Human Hair Lace Closure Wigs, 150% Density Straight Human Hair Wigs Pre-Plucked with Baby Hair Natural Color (16 Inch)
24. [All Beauty] Laine Synthetic Wig By Rene Of Paris Creamy Blonde
25. [All Beauty] Long Wavy Wig
26. [All Beauty] MOCOO 24 inch Straight Long Beautiful Red Hair Wigs Heat Resistant Synthectic Wig for Women with Natural Looking JF050
27. [All Beauty] Monikahair Bob Wig for Black Women Ombre Bob Wigs Highlight Purple Middle Part Synthetic Hair Wigs Natural Looking Heat Resistant Fiber for Party
28. [All Beauty] MowigLux Short Wavy Bob Wigs for Women Burgundy Color Synthetic Lace Wigs Heat Resistant Fiber Curly Bob Wigs 118 Color
29. [All Beauty] NOBLE Fashion Pixie Wigs Human Hair for Black Women Natural Pixie Cut Wigs Human Hair for Ladies Dark Brown Short Human Hair Wigs
30. [All Beauty] Ombre Purple Lace Front Wig with L Part Glueless Wavy Long Wigs for Women Synthetic Lace Wig with Natural Hairline
31. [All Beauty] OneUstar Women's Straight Red Wig Synthetic Cosplay Wig Party Wig With Free Wig Cap
32. [All Beauty] PATTNIUM 14 Inch Shoulder Length Wig Short Wavy Wig Multicolor Wig for Women and Girls Cosplay Costume Wig (Highlight Pink Mix Blue)
33. [All Beauty] SOMIARIK Highlight Pink Straight Synthetic Lace Front Wigs Highlight Pink Natural Straight Lace Front Wigs for Women Middle Part 150% Density Balayage Heat Resistant Hair Replacement Wigs (26 inches)
34. [All Beauty] Short Bob Wavy Curly Wig 14 inch Synthetic Wavy Wigs Shoulder Length Wigs for Women Costume Wigs for Daily Cosplay Use (14 Inch, Pink mix Blue)
35. [All Beauty] Short Headband Wigs for Black Women Afro Kinky Curly Wigs Head Wrap Wig 2 in 1 Wig Synthetic Natural Black Wigs with Bangs Short Curly Wigs with Headband (Leopard Turban Wig)
36. [All Beauty] Stamped Glorious Green Wig Short Wavy Wig Middle Part Wig Bob Synthetic Shoulder Length Wigs for Women Halloween Cosplay
37. [All Beauty] Stamped Glorious Short Wavy Bob Wig Synthetic Wine Red Color Wigs with Bangs for Women Shoulder Length Heat Resistant Fiber Wigs (Burgundy)
38. [All Beauty] Straight Lace Front Wigs Human Hair Brazilian Virgin Human Hair Lace Frontal Wigs Pre Plucked with Baby Hair 150 Density Wigs for Black Women Human Hair Natural Color (18 Inch)
39. [All Beauty] SureWells Costume Wigs Uta no Prince SAMA Shining Orange Wigs Cosplay Wigs Party Wigs Costume Wigs
40. [All Beauty] TSNOMORE Headband Wigs for Black Women, 26in Long Straight Black Black Headband Wig, 180% Density Full Ends Black Wig (Straight)
41. [All Beauty] TopWigy Short Royal Blue Wig, Curly Wave Wigs with Bangs, Fluffy Colorful Shoulder Length Synthetic Heat Resistant Hair for Costume Cosplay Daily Use(Bright Royal Blue,14")
42. [All Beauty] UU-Style Halloween Cosplay Womens Mioda Ibuki Horn Long Straight Cosplay Wigs Grey
43. [All Beauty] WIGNEE 100% Human Hair Short Wigs For Women Mommy Short Finger Wave Style Short Deep Wave Wigs For Black Women Clearance
44. [All Beauty] WIGODDESS Beige Color Synthetic Curly Wig, Curly Wig Daily Makeup Party Wig Perruque Heat Resistant Hair 24 inch Synthetic Lace Front T Part Curly Wig Daily Queen Makeup Gift For Women
45. [All Beauty] Women Ombre Blonde Wigs with Bangs Natural Wave Middle Length Curly Heat Resistant Synthetic Wig
46. [All Beauty] Women's Light Purple Wavy Wig with Bangs Middle Length Synthetic Wigs for Daily Use or Costume
47. [All Beauty] XSZM Highlight Lace Front Wigs Human Hair Pre Plucked Ombre Honey Blonde Body Wave Wig With Baby Hair Brazilian Ombre Brown Remy Bleached Knots Hair Deep T-Middle Part Wig for Women,12 Inch
48. [All Beauty] ZURO Black Bob Wig With Bangs Deep Wave Short Hair Wigs for Women Daily Use Purple Hot Pink Dark Brown Blonde Heat Resistant Synthetic Soft Cute Costume Wigs Shoulder Length Wavy Colorful Cosplay Wigs for Girls
49. [All Beauty] aSulis Hair Short Wave Wigs For Women Pink Synthetic Wig Shoulder Length Wig Middle Part Natural Black Bob Pastel Wavy Wigs for Halloween Cosplay Party Daily Use (Curly Wavy - Pink)
50. [All Beauty] piaou 28 Inches Ginger Orange Wig with Bangs Long Water Wave Hairstyle Wigs For Women Synthetic Wigs Long Natural Wave Heat Resistant Hair Wigs for Daily Party Cosplay

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 17
Cluster size: 198

Representative product titles:
1. [All Beauty] 112 Pieces Hair Silicone Curler Rollers Blue and Pink Hair Curlers Rollers Silicone Set Including 56 Pieces Large Size and 56 Pieces Small Size, with a Transparent Zipper Bag
2. [All Beauty] 18Pcs Magic Hair Curlers Spiral Curls No Heat Wave Hair Curler Styling Kits with Styling Hooks, for Most Kinds of Hairstyles 22"(55 cm) Long
3. [All Beauty] 2 in 1 Ionic Hair Straightening Brush for Short Hair, Portable and Dual Voltage for Travel, 30s MCH Rapid Heating ,Anti-Scald and Auto-Off, Best Gift for Family and Friend
4. [All Beauty] 20-packs 9.5" Twist-Flex Foam Hair Rollers Flexible Curing Rods for Long,Medium and Short Hair -No Heat Hair Curlers for Women's （Diameter 2cm）
5. [All Beauty] 31 Pieces Large Silicone Hair Curlers Set, 30 Pack Magic Hair Rollers 1.9 Inch No Clip Silicone Curlers with a Black Storage Bag for Women and Kids (Large)
6. [All Beauty] 32PCS Hair Curlers Hair Rollers Spiral Curls No Heat Hair Wavers Styling Kit Wave Magic Rollers for Short Hair Long Hair Medium Hair
7. [All Beauty] 36 Pcs Magic Hair Roller Curlers Heatless Styling Kit with 2 Pcs Hair Hooks for Women Girls (9.8inches)
8. [All Beauty] 40 Pieces Hair Curlers Spiral Curls Styling Kit Hair Rollers Flexible No Heat Hair Curlers Heatless with Hooks for Women Girls Kid Extra Long Hair Styling Tools from 22 Inch to 30 Inch
9. [All Beauty] 42 Pack Twist-flex Rods 7 Sizes Flexible Curl Sponge Flexi Hair Roller Set Hair Foam Curler Hot Roller Set(Random Color)
10. [All Beauty] 80pcs Perm Rods Long Cold Wave Rods 6 Size Perm Rod for Natural Hair Jumbo Large Medium Small Hair Roller Curling Rods DIY Hair Curlers for Long Short Hair(Blue+Orange+Beige+Purple+Grey+White)
11. [All Beauty] AnHua Women Professional Long Lasting Automatic Electric Heated Eyelash Curler (Pink)
12. [All Beauty] B-Qtech Flat Iron Cordless Hair Straightener (Yellow)
13. [All Beauty] BeVarious Curls Styling Kit, 20 No Heat Hair Curlers and 1 Styling Hooks Magic Hair Curlers Spiral Curls Styling Kit Easily Create Beautiful Curly Hair Suitable for long hair up to 22" (55 cm)
14. [All Beauty] Curling iron BESTOPE 1 Inch flat iron 2 in 1 Round Curling wand Ceramic Tourmaline iron Great Hair Straightener Set
15. [All Beauty] Deep Conditioning Heat Cap Electric Hair Nourishing Steamer Cap For Hair Spa Home Hair Thermal Treatment Beauty Spa US PLUG
16. [All Beauty] DrunkenCalf 24 Pieces No Heat Wave Hair Curlers Styling Kit Spiral Hair Curlers Hair Curlers Spiral Curls with 2 Pieces Styling Hooks for Most Kinds of Hairstyles (30cm/11.8inches,2 colors)
17. [All Beauty] Electric Hair Comb, Quick Beard Straightener Styling Comb Hair Curlers, Hair Straightener, Magic Massage Comb Beard Straightener Multi-functional Hair Comb Electric Hair Tool for Men (dark blue)
18. [All Beauty] FOYOCER Heatless Hair Curlers Rollers DIY Magic Hair Rollers for Short Long Hair
19. [All Beauty] Hair Curlers Spiral Curls Large Hair Rollers Wavy Hair Curler - Self Grip Self Grip and No Heat Hair Styling Kit for Most Kinds Of Hairstyles With 2 Magic Wands (28 Pcs, 20cm)
20. [All Beauty] Hair Curling Iron 3 Barrel Waver Iron Wand Fast Heating With LCD Temperature Display 176°F To 410°F Ceramic Wave Hair Iron Roller
21. [All Beauty] Hair Dryer Brush, Blow Dryer Brush 3-in-1 Hair Dryer and Styler Volumizer with Negative Ionic for Fast Drying, Straightening, Inner Curling, Anti-frizz Hot Air Brush with 3 Adjustment Modes
22. [All Beauty] Hair Dryer, slopehill Professional Salon Negative Ions Hair Blow Dryer for Fast Drying, Lightweight Bioceramic with Powerful Hot/Cool Wind, 3 Magnetic Attachments,UL Approved
23. [All Beauty] Hair Straightener Brush, AutoYet2 with 2-in-1 straightening Comb for Straightener and Curly Hair, Anti-Scald Heated Function Fast Heating instyler Rotating Iron for All Hair Types,Black(ATYT300B)
24. [All Beauty] Heatless Curling Rod Headband, Silk Soft Heatless Curls Roller Ribbon Headband, Sleeping Overnight Heatless Hair curlers, DIY Hair Styling Tools for Long Medium Hair (Pink)
25. [All Beauty] Heatless Curls,leeping Heatless Hair Curler,No Heat Hair Curlers For Long Hair,Heatless Curls Hair Rollers Set, Gifts For Women(Purple)
26. [All Beauty] Heatless Hair Curler Rollers, No Heat Flexible Curling Rods Overnight Sleep Styler for Women Natural Long Hair Silk Ribbon Curls with Soft Hairband Scrunchie Clips Tie Set, Gold Absorbent Formers
27. [All Beauty] Heatless Hair Curlers For Long Hair, No Heat Silk Curls Headband You Can To Sleep In Overnight, Soft Foam Hair Rollers, Curling Ribbon and Flexi Rods for Natural Hair (blue)
28. [All Beauty] Hot & Hotter Salon Ceramic Ionic Hood Dryer #5916
29. [All Beauty] HuaShanDa Heatless Curling Rod Headband, Tiktok Hair Curlers for Long Hair, Curler You Can To Sleep In Overnight, No Heat Curls Headband Natural Hair-Gifts Women, Pink, 6 Piece Set
30. [All Beauty] Ionic Hair Straightener Brush - Enhanced Ionic Straightening Brush with 13 Heat Levels for Frizz-Free Silky Hair, Anti-Scald & Auto-Off Safe & Easy to Use
31. [All Beauty] Jose Eber Vibrating 1.5" Flat Iron Hair Straightener Iron Innovative vibrating technology Real-time oscillation Dual voltage 110V/240V (Champagne)
32. [All Beauty] Keledz Hair Straightener Brush, Ionic Ceramic Fast Hair Straightening Comb with 5 Heating Setting Heating Function and LED Display, Anti Scald Ionic Brush (Black)
33. [All Beauty] Kissbeauty Chopstick Curling Wand Professional Salon 360°c Rotating Clip Ceramic Mini Hair Curling Iron.Small Barrels for Short Hair,Hair Curler,Hair Curling Wand (7MM) - Heat Protection Glove
34. [All Beauty] NewPollar Professional Hair Curling Iron Hot Brush Ionic Styler Styling Comb and Hair curler Heated Round Brush
35. [All Beauty] Parvella Heatless Curls Hair Curlers For Long Hair, Silk Heatless Curling Rod Headband, No Heat Soft Foam Hair Rollers Sleep, Curling Ribbon Hair Rope for Heatless Curls
36. [All Beauty] Professional Hair Straightener Brush for All Hair Types, YCDLEVAO Ionic Hair Straightening Brush Super Silky Smooth, Fast Ceramic Heating and Anti-Scald Comb
37. [All Beauty] QMSILR 2Pcs Hair Rollers with Tongs Self Grip Hair Curlers Rollers Curler Bangs Hair Sticky Hairdressing Curlers Plastic DIY Hair Styling Accessories Tools for Women Purple
38. [All Beauty] Roll On Wax Warmer with Double Cartridges, Professional Hair Removal Wax Heaters Hair Roller Epilator Wax Machine - Pink
39. [All Beauty] Steam Flat Iron Hair Straightener for Argan Oil Infusion Treatment,1 Inch Professional Ceramic Hair Straightener with,Repair Hair Damage,Auto Shut-Off and Dual Voltage (Black)
40. [All Beauty] TIGI Hardcore Tourmaline Smooth Operator Ceramic Flat Iron
41. [All Beauty] Tangobird Hair Rollers (36 PACK - 12 XL | 12 L | 12 M) | Jumbo Hair Rollers Hair Curlers For Long Hair | Self Grip Rollers For Hair | Heatless Hair Curlers For Long Hair with Travel Bag & Pins
42. [All Beauty] Titania Copper Round Styling Hair Brush - Premium Styling & Hairblowing Hairbrush w/Black Satin Handle & Nylon Pins - Improves Straight, Curly & Fine Natural Hair, Extensions & Wigs
43. [All Beauty] TraderPlus 42-Pack 7" Foam Curling Rollers Rods, Twist and Flex Hair Curlers
44. [All Beauty] Tru Beauty, 1.25-inch LED Curling Iron with Ceramic Coated Barrel for Women & All Hair Types & Lengths- White
45. [All Beauty] Twis-Les Electrical Cord Cover & Detangler - BLUE
46. [All Beauty] USpicy Hair Straightening Brush with Negative Ions Technology And Slide Temperature Control (Heats up Fast, Auto-Lock Function & Auto-Shut-Off Function, Innovative Bristle Design)
47. [All Beauty] WESOPAN Hair Waver for Deep Waves, Crimper Hair Iron Curling Barrel Fast Heating Ceramic Beach Waver Curler
48. [All Beauty] Wax Warmer Hair Removal Waxing Kit Constant Temperature Setting Electric Wax Heater Pot with 4 Flavors Wax Beans
49. [All Beauty] Wazor 1875W Hair Dryer Ceramic Negative Ionic Blow Dryer With 2 Speed and 3 Heat Settings Cool Shot Button Red
50. [All Beauty] interhasa! 1200W Wall Mount Hair dryer for bathroom hotel

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 18
Cluster size: 154

Representative product titles:
1. [All Beauty] 212 Assorted Halloween Kids Temporary Tattoo, Konsait Funny Colorful Monsters Temporary Tattoos for Children Boys Girls Kids Party Bag Filler and Gift for Halloween Party Favor Supplies Decoration
2. [All Beauty] 4 Bottles Temporary Tattoo Ink with 92pcs Tattoo Stencils, Waterproof Temporary Tattoo Kit for Men and Women, Semi Permanent Tattoo
3. [All Beauty] 5 large tribe totem tattoo stickers for men and women Black Medium / large body art make-up Fake Tattoo waterproof detachable (4.7x7.5inch)
4. [All Beauty] 5 x Daddy's Card - Princess, Yes Daddy, Property of Daddy - Temporary Fetish Daddy Girl Tattoo Set (5)
5. [All Beauty] 6 Sheet Cute Temporary Tattoos for Kids, My Little Pony Party Supplies Unicorn Ponies Party Favors Fake Sticker for Kids Boy Girl Pony Party Decoration School Rewards Birthday Gifts Water Bottle Decor
6. [All Beauty] 6 Sheets Women Men Body Art Tattoo Temporary Small Pattern Sticker Paper Unique Gift
7. [All Beauty] 60 Sheets Animals Theme Temporary Tattoos for Kids, Animal Tattoos Featured Zoo Patterned Body Art Waterproof Temporary Tattoos Toddler Tattoos, Fake Waterproof Tattoos for Boys Girls
8. [All Beauty] 68PCS Sonic Temporary Tattoos Sticker, The Cartoon Hedgehong Tattoos for Party Favor Gift Boy Children Birthday Kids Party Decoration
9. [All Beauty] 8 Sheets Cute Cartton Tattoos Kawaii Temporary Stickers for Girls Gift Bags Birthday Party Supplies
10. [All Beauty] 9 Sheets Rainbow Tattoos Rainbow Stickers Temporary Waterproof Tattoos for Pride Parades and Celebrations
11. [All Beauty] Adorable Butterfly Party Favors ~ 2 Dozen (24) Butterfly Pencils & 12 Dozen (144) Butterfly Temporary Tattoos - Goody Bags - Classroom Student Rewards ~ Peace Love Hippie Retro 60's
12. [All Beauty] Anself Black Electric Tattoo Ink Mixer Pigment Agitator Tattoo Machine Supply Tool With 5 Sticks
13. [All Beauty] Ben Nye Tattoo Cover (NT-1)
14. [All Beauty] COKOHAPPY 2 Sets Mermaid Face Hair Gems Festival Jewels Temporary Tattoos Self Adhesive Bindi Rhinestone Glitter Sticker Crystal for Eyes Face Body Rave Makeup Party Decoration (Collection 3)
15. [All Beauty] Chuse 10PCS 9RS Disposable Tattoo and Permanent Makeup Needles
16. [All Beauty] Day of the Dead Face Skeleton Tattoos(36 Sheets), Halloween Temporary face Tattoos, Skull Face Tattoo, Red Rose Face Decor Tattoo, Fake Wounds, Scars Stickers for Halloween Party Favor Zombies Cosplay
17. [All Beauty] Dopetattoo 6 Sheets Temporary Tattoos Peach Fake tattoos Neck Arm Chest for Women Men Adults 3.7 X 3.7 Inch
18. [All Beauty] Dragonhawk 4 Standard Tunings Tattoo Machines Fine Lining Shading Machine Lining Machine Coloring Machine
19. [All Beauty] Easter Tattoos For Kids Easter Temporary Tattoos Eggs Bunny Chicken Cute Cartoon Easter Tattoo Stickers Decoration For Easter Party Favors Kids (4-Easter)
20. [All Beauty] Face Gems, Ynredee 2 Set Women Mermaid Rave Festival Glitter, Rhinestone Temporary Tattoo Face Jewels Crystals Face Stickers Eyebrow Face Body Jewelry for Halloween, Christmas, All Saints' Day
21. [All Beauty] Face Paint Kit for Kids, 15 Colors Water Based Face Body Painting Palette with 2 Brushes 4 Sheets Stencils, Professional Halloween, Festivals, Theater, Special Effects Makeup Kit
22. [All Beauty] Fing'rs Prints Ghoulish Glam Vampy Vixen
23. [All Beauty] Fleur de lis
24. [All Beauty] Footprint Black Big Feet Tattoo Stickers Temporary Tattoos 3pcs/lot 17.8cm X 10cm
25. [All Beauty] Golden Kiss set of 25 premium waterproof metallic gold lip temporary foil Flash Tattoos - use for girls night out, party favors, bachelorette parties, showers and more!
26. [All Beauty] Grier Luau Themed Temporary Tattoos Party Decorations for Kids and Adults,Hawaiian Summer Beach Pool Tattoos Party Favors
27. [All Beauty] Halloween Scar Temporary Tattoo Sticker Fake Blood Vampire Wound Stitch Water Transfer Decal Horror Face Body Tattoo Perfect for Halloween, Party, Cosplay, Costume Accessories, Masquerade 9 Large Sheets
28. [All Beauty] Halloween temporary tattoo spider and spider web water transfer waterproof tattoo atmosphere stickers party cosplay 10pcs
29. [All Beauty] JBCD 5 Pcs Maryland Flag Tattoos MD Flag Stickers Face Tattoos, State Tattoos Temporary Decorations Suitable for Sports Event and Party
30. [All Beauty] Konsait Bachelorette Party Tattoos Metallic Tattoos(100+ Designs),Bride Tattoos Bride Tribe Gold Foil Temporary Tattoos for Bridal Shower Bachelorette Bridal Shower Party Favor Supplies
31. [All Beauty] Metallic Temporary Tattoos - 12 Sheets Waterproof Gold Sliver Glitter Body Face Tattoo for Women Teen Girls, Over 200 Flash Fake Festival Jewelry Bling Body Art Tat Stickers
32. [All Beauty] Penguin Tub Tattoos
33. [All Beauty] Prefilled Jumbo Easter Eggs with Tattoos, Finding Dory - Easter Basket Stuffers 3 Pack
34. [All Beauty] Q&Q Fashion Fallen Angel Wings Raver Arm Leg Body Art Waterproof Temporary Tattoo Sticker
35. [All Beauty] Ruby Red Face Paint Stamps - Kitten
36. [All Beauty] SHENGHUO Halloween Sleeve Temporary Tattoos 6-Sheet, Death Skull Tatoos Black Body Tattoo Stickers for Adults, Men, Women, Girls, Kids, Halloween Parties Makeup
37. [All Beauty] SKULLS VARIETY SET of 24 assorted premium waterproof metallic gold and silver jewelry temporary foil party Flash Tattoos - skull tattoo, Halloween party, sugar skull, party supplies
38. [All Beauty] Small Tattoos Black Realistic Temporary Tattoos for Women Men Adults Waterproof Tiny Fake Tattoos Body Stickers Word Cross Anchor Flower Temp Tattoo Paper Finger Neck Wrist Ankle Tattoo (40 Sheets)
39. [All Beauty] St. Patrick's Day Tattoo Sticker Festival Party Waterproof Clover Decor
40. [All Beauty] Tatoodle - Temporary Illustrated Artistic Tattoos - Christmas Lights
41. [All Beauty] Tattify Joy Division Temporary Tattoo - The Great Unknown (Set of 2) - Other Styles Available - Fashionable Temporary Tattoos - Long Lasting and Waterproof
42. [All Beauty] Tattify Sci-Fi Temporary Tattoos - Doctor Who (Set of 24 Tattoos- 2 of each Style) Individual Styles Available - Fashionable Temporary Tattoos
43. [All Beauty] Temporary Tattoo Factory Stripteaze Naughty Tattoos - Naughty Ultra Realistic Fake Adult Temporary Tattoos a little Trashy and Slutty Words Tattoos for Women's Hip, Lower Back, Thigh, Arm Tramp Stamp - Long Lasting (30Pack)
44. [All Beauty] Temporary Tattoo Kit, Freehand Ink Semi Permanent Tattoo, 5 Colors and 114Pcs Adhesive Stencils, DIY Tattoos Inkbox for Women Kids Men Body Markers - Full Kit 5 Bottles (Black/Brown/Red/Blue/Purple)
45. [All Beauty] Temporary Tattoos for Kids, Konsait 250+pcs Glow In The Dark Mixed Style Cartoon Tattoo, Luminous Unicorn Mermaid Butterfly Shark Sweet Pirate Car Game Tattoos for Boys Girls Birthday Party Favors
46. [All Beauty] Tiktok Ins Baby Hair Tattoo Stickers Temporary Edges Curly Black with Highlights Baby Hair Tattoo 7PC+4PC 4 Eyeshadow Pads
47. [All Beauty] WEGOTTABB 6 sheets 6D Hairlike Eyebrow Tattoo Sticker Black Waterproof Grooming Shaping Eyebrow Sticker in Arch Style for Women and Girls,60 pairs (Elegent Styels(QZ))
48. [All Beauty] Willie Tattoos With Willie Sponge - 10 Pack
49. [All Beauty] Wyuen 12 PCS/lot Wolf Temporary Tattoo Sticker for Women Men Fashion Body Art Adults Waterproof Hand Fake Tatoo 9.8X6cm FW12-01 (Fox)
50. [All Beauty] glaryyears Wound Tattoo for Halloween Party (50 Sheets, over 300 patterns) Temporary Tattoos for Women Men Halloween decorations 2.4''x4.1''

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
I clustered ecommerce products using KMeans on template Jina embeddings.

Review the representative product titles from one cluster and assign a taxonomy label.

Cluster ID: 19
Cluster size: 369

Representative product titles:
1. [All Beauty] 10 Pairs Waterproof Magnetic Lashes Kit With Gold Collagen Eye Pads l Super Strong Magnets l Natural Looking Eyelashes l Magnetic Eyelashes With Eyeliner l Magnetic Lashes
2. [All Beauty] 100 Pieces Empty Eyelashes Packaging Paper Case Eyelash Holder Box Eyelashes Container with Holographic Design for False Eyelash Care Cosmetic Tools
3. [All Beauty] 100 Pieces Empty Eyelashes Packaging Paper Lash Box, 50 Empty Eyelash Boxes Lash Box Packaging Empty Lash Box with 50 Empty Eyelash Boxes Tray False Eyelashes Storage Box Lid Tray(Blue Butterfly)
4. [All Beauty] 12 Packs Eyelashes - #747S (Christina)…
5. [All Beauty] 18 Pairs Lashes 6 Styles Lashes Pack Natural Look Wispy 3D Volume Faux Mink Lashes Dramatic Fluffy Soft Handmade Reusable Lashes Pack
6. [All Beauty] 20 Pairs 2 Styles Mixed False Eyelashes ALPHONSE Fluffy Luxurious Cat-Eye Fake Eyelashes 3D Crossed Volume Dramatic Faux Mink Lashes Pack
7. [All Beauty] 20 Pairs False Eyelashes 4 Styles Mixed Fluffy Cat-Eye Wispy Lashes ALPHONSE 3D Volume Luxurious Faux Mink Eyelashes Pack
8. [All Beauty] 2400 Pcs Invisible Double Eyelid Tape Stickers, Breathable Lift Double Eyelid Stickers, Double Eyelid Tape Tool for Hooded Droopy Eyes, Easy to Make Up,Waterproof Sweatproof
9. [All Beauty] 316L Bike Essential Oil Diffuser Aromatherapy Locket Necklace
10. [All Beauty] 3D Mink Lashes 25mm Lashes Handmade Volume Thick Mink Eyelashes 3 Pairs Ruairie
11. [All Beauty] 400pcs Eyelid Tape, Breathable and Waterproof Eyelid Lifter Strips, Invisible Lids by Design Double Eyelid Strips with Fork Rods and Tweezers for Droopy, Uneven, Hooded Eyes
12. [All Beauty] 5 Style Mix 10 Pairs False Eyelashes Natural Look 3D Fake Lashes Small Face Eyelashes 100% Handmade Lashes Wispies Short Soft Reusable Eye Lash Transparent Band Eyelash 1 Pack by EMEDA
13. [All Beauty] 6 Pieces Double Layer Eyelash Packaging Circle Box Eyelash Storage Box Case Lash Boxes Empty Lash Case with Mirror and Tray for Women Girls, Rose Red
14. [All Beauty] 8 Pieces False Eyelashe Applicator Tool, Stainless Steel Eyelash Extension Tweezers Remover Clip Stainless Steel Nipper Tool
15. [All Beauty] ALICROWN Lashes Faux Mink Fluffy Lashes 3D Volume Natural Fluffy Lashes Pack False Eyelashes Natural Look
16. [All Beauty] Ardell Faux Mink #813 Black Lashes (2 Pack)
17. [All Beauty] Cat Eye Lashes Pack False Eyelashes Full Fluffy Medium Volume 3D Faux Mink Lashes Wispy 4 Styles 17-19mm Soft Reusable Handmade Fake Eyelashes, 16 Pairs Pack by Pawotence
18. [All Beauty] Classic Lash Extensions D Curl 0.15 Mixed Tray 14-20mm Matte Mink Eyelashes
19. [All Beauty] Ellipse Eyelash Extensions 0.15-D Curl 11mm Flat Light Lashes Matte Individual Eyelashes Salon Use 0.15/0.20mm C/CC/D/DD Curl Single 8-16mm Mix 8-15mm（0.15 D 11mm)
20. [All Beauty] Eyelash Extension BL Lash 5D Volume Lash C Curl Thickness 0.07mm (0.07X11mm)
21. [All Beauty] Eyelash Extension Supplies 0.05 D Curl 13mm Individual Lash Extensions Silk Professional Salon New Material|0.03/0.05/0.07/0.10/0.15/0.20 C/D Curl 10-16mm Mix 8-15mm|(0.05 D 13mm)
22. [All Beauty] Faith Beauty Longer Dual Magnet False Eyelash (Dual Magnet,)
23. [All Beauty] False Eyelashes ALICE 25MM Dramatic Faux Mink Lashes Pack 8 Pairs 8 Styles Fluffy Long Strip Fake Eyelashes Thick Volume Crossed 3D Eye Lashes
24. [All Beauty] False Eyelashes,Laimeng A Pair Natural Beauty Dense False Eyelashes
25. [All Beauty] False-Lashes 3-Pairs-of-Self-Adhesive-Fake-Eyelashes Friendly-to-First-Time-User No-Glue-or-Eyeliner-Needed Waterproof-Reusable-and-Natural-Look
26. [All Beauty] Flat Lashes C Curl 0.20mm 8-14mm Mixed Tray Ellipse Eyelash Extensions Volume Lashes Individual 3D Salon Perfect Use by FADLASH
27. [All Beauty] Fyonas 3D Mink Eyelashes 100% Siberian Mink Fur False Lashes Strip Eyelashes,Halloween, Christmas Theme Fake Eyelashes(F22)
28. [All Beauty] Homtone 3 Layers Acrylic False Eyelash Organizer Case Display Box for 18 Pairs Eyelashes Transparent Storage Box, Size 6.7x4.7x2.5inch
29. [All Beauty] JIMIRE 14 Styles Mixed False Eyelashes Fluffy Fake Lashes Natural 3D Volume Faux Mink Lashes Pack
30. [All Beauty] MISMXC False Eyelashes Extension Practice Exercise Set, Professional Mannequin Head Lip Makeup Eyelash Grafting Training Tool Kit for Makeup Practice Eye Lashes Grafting
31. [All Beauty] MISMXC Magnetic Eyeliner and Eyelashes Kit,Upgraded 3D Magnetic Eyelashes and Eyeliner Set with 10 Pairs Reusable Magnetic Lashes &2 Tubes of Magnetic Eyeliner&1 Tweezers-No Glue Need
32. [All Beauty] Magnet Eyelashes-Dual Magnetic False Eyelashes with NO GLUE 3D Fiber Reusable Best Fake Lashes Extension for Natural Look,Perfect for Deep Set Eyes (-2 Pair/8 Pieces) (DUAL-FULL SZIE 014)
33. [All Beauty] Magnetic Eyelash with Eyeliner,10 Pairs of Reusable Magnetic lashes and Highly Imitation 5D Mink Hair Eyelashes，Magnetic Eyelash Kit Natural Look, Waterproof Liquid Eyelashes, No Glue Needed
34. [All Beauty] Magnetic Eyelashes Kit,Magnetic Eyelashes and Eyeliner Kit,with Most Natural Look,12 Pairs Magnetic Eyelashes & 3 Magnetic Eyeliner,Reusable Magnetic Eyelashes,No Glue Need
35. [All Beauty] Magnetic Eyelashes Kits Set, 2019 Minso Natural-looking Design Magnetic Eyelashes with Magnetic Liquid Eyeliner and Delicate -box ，Easy-wearing & Reusable Eyelashes
36. [All Beauty] Magnetic Eyelashes Magnetic Eyeliner Kit Magnetic Eyeliner and Lashes Magnetic Eyelashes Kit False Lashes 3D Reusable Lash Liner Extension (3-Pairs)
37. [All Beauty] Magnetic Eyelashes with Eyeliner - Magnetic Eyelashes Natural Look with 2 Tubes Eyeliner Kits Tweezers, Eyelashes Magnetic Lashes Natural, Waterproof, No Glue Needed, Easy to Wear(10 Pairs )
38. [All Beauty] Magnetic Eyelashes with Eyeliner - Magnetic Eyeliner and Magnetic Eyelash Kit - Eyelashes With Natural Look - Comes With Applicator - No Glue Needed (Diamond-5)
39. [All Beauty] Magnetic False Eyelashes,5 Pairs of Updated 3D 5D 6D 8D Magnetic Lashes and 2 Tubes of Magnetic Eyeliner (with Tweezers),Natural Look and Reusable False Eyelashes,No Glue Needed
40. [All Beauty] Mascara Waterproof Mascara, 4D Silk Fiber Lash Mascara Black for Longer, Thicker, Voluminous Eyelashes, Natural 4D Gel and Fibers Formula
41. [All Beauty] Mirenesse Magnomatic 24hr Magnetic Eyeliner & Reusable 5D False Lashes,Safe. Easy No Adhesive No Mess, Vegan & Toxin Free, 2 Pairs Volume Vivian Day & Night + Magnetic Liner 0.17oz
42. [All Beauty] New Japanese Style Black 10 Pairs Asia Eyelashes Clearance sale (10 Pairs, Black)
43. [All Beauty] Non Magnetic Eyeliner and Eyelashes Kit, Magic Self Adhesive False Eyelashes and Eyeliner, 5 Pairs 5D Reusable False Lashes with No Glue, Waterproof Lash Boxes with Mirror & Tweezers
44. [All Beauty] Pawotence False Eyelashes 25mm Dramatic Long Faux Mink Lashes Pack 10 Pairs Soft Handmade Fake Eyelashes Pack
45. [All Beauty] QUEWEL Volume Eyelash Extensions | 0.03-0.12mm | C/CC/D/DD Curl | 8-25mm Length | Easy Fan Volume Lashes 2D-20D Self Fanning Volume Lashes 0.10CC Mix-8-15mm Long Lasting Blooming Lashes(0.10CC Mix8-15)
46. [All Beauty] Ultra Invisible Double Eyelid Tape Stickers - 200Pcs/100Pairs Both Side Sticky Instant Eye Lid Lift Strips - Perfect for Hooded Droopy Uneven or Mono-eyelids
47. [All Beauty] WEYZIM 3D Faux Mink Lashes 2 Pairs Handmade Luxurious Volume Fluffy Natural False Eyelashes Reusable 100% Handmade 3D02
48. [All Beauty] Wleec Beauty 3D Silk Lashes Handmade Natural False Eyelash Pack #3D/19 (15 Pairs/3 Pack)
49. [All Beauty] Y-KINZ Upgraded Invisible Magnetic Eyelashes and Eyeliner Kit False Lashes With Applicator Tool， No Magnet Block on Eyelashes Waterproof Long Lasting Reusable No Glue Needed[6 Pairs]
50. [All Beauty] wiwoseo False Eyelashes Faux Mink Lashes 7 Pairs Pack Dramatic Fake Eyelashes Long Fluffy Thick Crossed Eye Lashes Multipack

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

