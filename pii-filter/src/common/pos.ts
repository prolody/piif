export namespace POS
{
    export class Tag
    {
        constructor(
            public tag_base: string,
            public tag_rest: Array<string>
        ) {};
    }

    export interface Tagger
    {
        tag(tokens: Array<string>): Array<[string, POS.Tag]>;
    };

    export function from_brill_pos_tag(tag: string): POS.Tag
    {
        let tag_base:           string =        tag;
        let tag_rest:           Array<string> = new Array<string>();
        let left_paren_index:   number =        tag.indexOf('(');
        let right_paren_index:  number =        tag.indexOf(')', left_paren_index);
        if (left_paren_index > -1 && right_paren_index > -1)
        {
            tag_base = tag.substr(0, left_paren_index);
            tag_rest = tag.substr(left_paren_index + 1, right_paren_index - left_paren_index - 1).split(',');
        }
        return new POS.Tag(
            tag_base,
            tag_rest
        );
    }
};