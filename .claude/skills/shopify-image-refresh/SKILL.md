---
name: shopify-image-refresh
description: Pick one Shopify product not already in the tracker, skip it if it has variants, otherwise regenerate images 2–4 in ChatGPT (Chrome) as white studio 3/4-left shots, delete images 5 and later, upload the new images, log the product, and report a done/remaining table. Use when the user runs /shopify-image-refresh or asks to "refresh the next product's images".
---

# Shopify Image Refresh

Handles **one product per run**. Tracker: `tracker.md`, in this skill's folder.

## Needs
- Shopify connector
- Claude in Chrome with ChatGPT signed in
- Dropbox connector
- Download folder: `E:\Dropbox\Downloads` (Dropbox path `/Downloads`)

## Steps

### 1. Pick a product
1. Read `tracker.md` and collect every Product ID in it.
2. Get products with Shopify `search_products`, `status:active`, sorted by TITLE, 50 per page. Follow `after` cursors until you find one whose ID is **not** in the tracker.
3. Update `Store total at last run` in the tracker with `productsCount`.

### 2. Check for variants
- The product **has variants** if `variantsCount > 1`, or its only variant title is not `Default Title`.
- If it has variants:
  1. Add a tracker row with Result `SKIPPED – has variants`.
  2. Go back to step 1 and pick the next product. Skipped products don't count as the run's product.

### 3. Plan the images (non-variant product only)
1. List the product's media in order with `graphql_query` on `product(id){ media(first:50){ nodes{ id alt mediaContentType preview{ image{ url } } } } }`.
2. **Image 1:** never touch it.
3. **Images 2–4:** regenerate them, one new image for each existing image. Don't create extra images if the product has fewer than 4.
4. **Images 5 and later:** mark them for deletion. No replacements.
5. If the product has only 1 image, go to step 6 and log it as `DONE – only 1 image`.

### 4. Generate in ChatGPT (Chrome)
For each image in slots 2–4:
1. Open https://chatgpt.com in Chrome and start a new chat.
2. Attach the original image. Download it from its URL first if needed.
3. Send this prompt:

   > Recreate this exact product as a professional e-commerce photo. Three-quarter angle view turned to the left. Clean white studio background, product standing on a white surface, soft even studio lighting with a gentle natural shadow. Well presented, vibrant true-to-life colors, sharp focus. Keep the product's shape, details, colors, text and proportions identical. No props, no text, no watermark. Square 1:1.

4. Wait for the result and download it to `E:\Dropbox\Downloads`.
5. Rename it to `<handle>-<slot>.png`, for example `giraffe-plush-2.png`.
6. Check the image. If the product looks wrong (shape, color or text changed), regenerate it once.

### 5. Upload to Shopify
1. **Get public links.** For each new file, use Dropbox `create_shared_link` on `/Downloads/<file>`. Change the link to a direct one (`dl=1`, or the `dl.dropboxusercontent.com` host).
2. **Upload.** Use `graphql_mutation` `productCreateMedia` with `originalSource` set to that URL, `mediaContentType: IMAGE`, and `alt` set to the product title.
3. **Wait for processing.** Poll until every new media is `READY`.
4. **Delete old images.** Use `productDeleteMedia` on the old slot 2–4 media and all media in slot 5 and later.
5. **Set the order.** Use `productReorderMedia` to put the original image 1 first, then the new images in slot order.
6. **Verify.** The product must have at most 4 images, with image 1 unchanged.

### 6. Log it
Append a row to `tracker.md`:
`| n | YYYY-MM-DD | gid://shopify/Product/… | Title | DONE – replaced X, removed Y |`

Write the row right after the upload succeeds, even if the report fails.

### 7. Report
Reply in this order:

1. **This run:** product title, admin link `https://admin.shopify.com/products/<numeric id>`, the new images, how many were replaced, and how many were removed.

2. **Progress table:**

   | | Count |
   |---|---|
   | Done (images refreshed) | … |
   | Skipped (has variants) | … |
   | Left to check | total − done − skipped |

3. **Done so far:** a list of every product title with Result `DONE`.

## Rules
- One product per run. Never reprocess a product that's already in the tracker.
- Never modify image 1, and never modify a product that has variants.
- If a step fails, don't mark the product `DONE`. Log it as `FAILED – <reason>` so it's visible, then remove that row before retrying.
