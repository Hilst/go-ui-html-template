package functions

import (
	html "html/template"

	"github.com/qri-io/jsonpointer"
)

func Map() html.FuncMap {
	return html.FuncMap{
		"array":      array,
		"dateformat": dateformat,
		"filter":     filter,
		"first":      first,
		"get":        get,
		"mask":       mask,
		"now":        now,
		"pad":        pad,
		"props":      props,
		"split":      split,
		"string":     stringfy,
		"timedate":   timedate,
	}
}

func get(path string, from any) any {
	p, perr := jsonpointer.Parse(path)
	if perr == nil {
		c, cerr := p.Eval(from)
		if cerr == nil {
			return c
		}
	}
	return nil
}