module.exports = {
    hooks: {
        "page:before": function (page) {
            let content = page.content;
            content = `>*Last modified: {{ file.mtime }}*\n\n${content}`; 
            page.content = content; 
            return page;
        }
    }
};
