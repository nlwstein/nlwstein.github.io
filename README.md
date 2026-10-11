# nlwstein.github.io 

Dynamic resume for [@nlwstein](https://github.com/nlwstein)

# View Resume

* Web version available at: https://cv.stein.boston
* Dynamically-generated PDF at https://cv.stein.boston/resume.pdf.

# How it works

Edit [config.yaml](config.yaml) (content) or [templates/resume.html.j2](templates/resume.html.j2) (layout) and push to `main`.
The [workflow](.github/workflows/generate.yaml) renders the HTML, prints the PDF with headless Chrome, and deploys both to GitHub Pages.
Built files are not committed. The custom domain is set in the repo's Pages settings.

Preview locally:

```sh
uv run --no-project --with-requirements requirements.txt generate.py > index.html
```
